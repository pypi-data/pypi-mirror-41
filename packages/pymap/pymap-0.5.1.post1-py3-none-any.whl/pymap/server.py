"""Defines socket interaction, accepting connections and handling a basic
command/response flow.

"""

import asyncio
import binascii
import re
from asyncio import IncompleteReadError, StreamReader, StreamWriter
from base64 import b64encode, b64decode
from ssl import SSLContext
from typing import List, Optional

from pysasl import ServerChallenge, AuthenticationError, \
    AuthenticationCredentials

from .bytes import as_memoryview
from .concurrent import Event, TimeoutError
from .config import IMAPConfig
from .context import current_command, socket_info
from .exceptions import ResponseError
from .interfaces.session import LoginProtocol
from .parsing.command import Command
from .parsing.commands import Commands
from .parsing.command.nonauth import AuthenticateCommand, LoginCommand, \
    StartTLSCommand
from .parsing.command.select import IdleCommand
from .parsing.exceptions import RequiresContinuation, BadCommand
from .parsing.response import ResponseContinuation, Response, ResponseCode, \
    ResponseBad, ResponseNo, ResponseBye, ResponseOk
from .sockinfo import SocketInfo
from .state import ConnectionState

__all__ = ['IMAPServer', 'IMAPConnection']


class Disconnected(Exception):
    """Thrown if the remote socket closes when the server expected input."""
    pass


class IMAPServer:
    """Callable object that creates and runs :class:`IMAPConnection` objects
    when :func:`asyncio.start_server` receives a new connection.

    Args:
        login: Login callback that takes authentication credentials and
            returns a :class:`~pymap.interfaces.session.SessionInterface`
            object.
        config: Settings to use for the IMAP server.

    """

    __slots__ = ['commands', 'login', 'config']

    def __init__(self, login: LoginProtocol, config: IMAPConfig) -> None:
        super().__init__()
        self.commands = config.commands
        self.login = login
        self.config = config

    async def __call__(self, reader: StreamReader,
                       writer: StreamWriter) -> None:
        conn = IMAPConnection(self.commands, self.config, reader, writer)
        state = ConnectionState(self.login, self.config)
        await conn.run(state)


class IMAPConnection:
    """Runs a single IMAP connection from start to finish.

    Args:
        commands: Defines the IMAP commands available to the connection.
        config: Settings to use for the IMAP connection.
        reader: The input stream for the socket.
        writer: The output stream for the socket.

    """

    __slots__ = ['commands', 'config', 'params', 'bad_command_limit',
                 '_print', 'reader', 'writer']

    def __init__(self, commands: Commands, config: IMAPConfig,
                 reader: StreamReader,
                 writer: StreamWriter) -> None:
        super().__init__()
        self.commands = commands
        self.config = config
        self.params = config.parsing_params
        self.bad_command_limit = config.bad_command_limit
        self._reset_streams(reader, writer)
        self._print = self._real_print if config.debug else self._noop_print

    def _reset_streams(self, reader: StreamReader, writer: StreamWriter):
        self.reader = reader
        self.writer = writer
        socket_info.set(SocketInfo(writer))

    @classmethod
    def _real_print(cls, prefix: str, output: bytes) -> None:
        prefix = prefix % socket_info.get().socket.fileno()
        lines = re.split(br'\r?\n', output)
        if not lines[-1]:
            lines = lines[:-1]
        for line in lines:
            line_str = str(line, 'utf-8', 'replace')
            print(prefix, line_str)

    @classmethod
    def _noop_print(cls, prefix: str, output: bytes) -> None:
        pass

    async def read_continuation(self, literal_length: int) -> bytes:
        try:
            extra_literal = await self.reader.readexactly(literal_length)
        except IncompleteReadError:
            raise Disconnected
        extra_line: bytes = await self.reader.readline()
        if self.reader.at_eof():
            raise Disconnected
        extra = extra_literal + extra_line
        self._print('%d -->|', extra)
        return as_memoryview(extra)

    async def authenticate(self, state: ConnectionState, mech_name: bytes) \
            -> Optional[AuthenticationCredentials]:
        mech = state.auth.get_server(mech_name)
        if not mech:
            return None
        responses: List[ServerChallenge] = []
        while True:
            try:
                return mech.server_attempt(responses)
            except ServerChallenge as chal:
                chal_bytes = b64encode(chal.get_challenge())
                cont = ResponseContinuation(chal_bytes)
                await self.write_response(cont)
                resp_bytes = await self.read_continuation(0)
                try:
                    chal.set_response(b64decode(resp_bytes))
                except binascii.Error as exc:
                    raise AuthenticationError(exc)
                if bytes(resp_bytes).rstrip(b'\r\n') == b'*':
                    raise AuthenticationError('Authentication canceled.')
                responses.append(chal)

    async def read_command(self) -> Command:
        line = as_memoryview(await self.reader.readline())
        if self.reader.at_eof():
            raise Disconnected
        self._print('%d -->|', line)
        conts: List[bytes] = []
        while True:
            try:
                cmd, _ = self.commands.parse(
                    line, self.params.copy(continuations=conts.copy()))
            except RequiresContinuation as req:
                cont = ResponseContinuation(req.message)
                await self.write_response(cont)
                ret = await self.read_continuation(req.literal_length)
                conts.append(ret)
            else:
                return cmd

    async def read_idle_done(self, cmd: IdleCommand) -> None:
        buf = await self.read_continuation(len(cmd.continuation))
        cmd.parse_done(buf, self.params.copy(tag=cmd.tag))

    async def write_response(self, resp: Response) -> None:
        raw = bytes(resp)
        self.writer.write(raw)
        await self.writer.drain()
        self._print('%d <--|', raw)

    async def start_tls(self, ssl_context: SSLContext) -> None:
        loop = asyncio.get_event_loop()
        transport = self.writer.transport
        protocol = transport.get_protocol()  # type: ignore
        new_transport = await loop.start_tls(  # type: ignore
            transport, protocol, ssl_context, server_side=True)
        protocol._stream_reader = StreamReader(loop=loop)
        protocol._client_connected_cb = self._reset_streams
        protocol.connection_made(new_transport)
        self._print('%d <->|', b'<TLS handshake>')

    async def send_error_disconnect(self) -> None:
        resp = ResponseBye(b'Unhandled server error.')
        try:
            await self.write_response(resp)
            self.writer.close()
        except IOError:
            pass

    async def write_bad_command(self, bad: BadCommand,
                                bad_commands: int) -> bool:
        resp = bad.get_response()
        if self.bad_command_limit and bad_commands >= self.bad_command_limit:
            bye = ResponseBye(b'Too many errors, disconnecting.')
            resp.add_untagged(bye)
        await self.write_response(resp)
        return resp.is_terminal

    async def write_updates(self, state: ConnectionState,
                            cmd: IdleCommand, done: Event) -> None:
        async for resp in state.receive_updates(cmd, done):
            await self.write_response(resp)

    async def idle(self, state: ConnectionState, cmd: IdleCommand) -> Response:
        response = await state.do_command(cmd)
        if not isinstance(response, ResponseOk):
            return response
        done = self.config.new_event()
        await self.write_response(ResponseContinuation(b'Idling.'))
        task = asyncio.create_task(self.write_updates(state, cmd, done))
        try:
            await self.read_idle_done(cmd)
        except BadCommand as bad:
            return bad.get_response()
        finally:
            done.set()
        await task
        return response

    async def run(self, state: ConnectionState) -> None:
        """Start the socket communication with the IMAP greeting, and then
        enter the command/response cycle.

        Args:
            state: Defines the interaction with the backend plugin.

        """
        self._print('%d +++|', bytes(socket_info.get()))
        bad_commands = 0
        try:
            greeting = await state.do_greeting()
        except ResponseError as exc:
            resp = exc.get_response(b'*')
            resp.condition = ResponseBye.condition
            await self.write_response(resp)
            self.writer.close()
            return
        else:
            await self.write_response(greeting)
        while True:
            try:
                cmd = await self.read_command()
            except BadCommand as bad:
                bad_commands += 1
                if await self.write_bad_command(bad, bad_commands):
                    break
            except (ConnectionResetError, BrokenPipeError):
                break
            except Disconnected:
                break
            except Exception:
                await self.send_error_disconnect()
                raise
            else:
                bad_commands = 0
                prev_cmd = current_command.set(cmd)
                try:
                    if isinstance(cmd, AuthenticateCommand):
                        creds = await self.authenticate(state, cmd.mech_name)
                        response = await state.do_authenticate(cmd, creds)
                    elif isinstance(cmd, LoginCommand):
                        creds = AuthenticationCredentials(
                            cmd.userid.decode('utf-8', 'surrogateescape'),
                            cmd.password.decode('utf-8', 'surrogateescape'))
                        response = await state.do_login(cmd, creds)
                    elif isinstance(cmd, IdleCommand):
                        response = await self.idle(state, cmd)
                    else:
                        response = await state.do_command(cmd)
                except ResponseError as exc:
                    resp = exc.get_response(cmd.tag)
                    await self.write_response(resp)
                    if resp.is_terminal:
                        break
                except AuthenticationError as exc:
                    msg = bytes(str(exc), 'utf-8', 'surrogateescape')
                    resp = ResponseBad(cmd.tag, msg)
                    await self.write_response(resp)
                except TimeoutError:
                    resp = ResponseNo(cmd.tag, b'Operation timed out.',
                                      ResponseCode.of(b'TIMEOUT'))
                    await self.write_response(resp)
                except Exception:
                    await self.send_error_disconnect()
                    raise
                else:
                    await self.write_response(response)
                    if response.is_terminal:
                        break
                    if isinstance(cmd, StartTLSCommand) and state.ssl_context \
                            and isinstance(response, ResponseOk):
                        await self.start_tls(state.ssl_context)
                finally:
                    current_command.reset(prev_cmd)
        self._print('%d ---|', b'<disconnected>')
        self.writer.close()
