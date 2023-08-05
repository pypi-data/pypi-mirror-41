from functools import total_ordering
from typing import Tuple, FrozenSet, AnyStr

from .. import NotParseable, Space, Params, Special
from ..primitives import Atom

__all__ = ['Flag', 'get_system_flags', 'Seen', 'Recent', 'Deleted', 'Flagged',
           'Answered', 'Draft']


@total_ordering
class Flag(Special[bytes]):
    """Represents a message flag from an IMAP stream.

    Args:
        value: The flag or keyword value.

    """

    def __init__(self, value: AnyStr) -> None:
        super().__init__()
        if isinstance(value, bytes):
            value_bytes = value
        else:
            value_bytes = bytes(value, 'ascii')
        self._value = self._capitalize(value_bytes)

    @property
    def value(self) -> bytes:
        """The flag or keyword value."""
        return self._value

    @property
    def is_system(self) -> bool:
        """True if the flag is an RFC-defined IMAP system flag."""
        return self.value.startswith(b'\\')

    @classmethod
    def _capitalize(cls, value: bytes) -> bytes:
        if value.startswith(b'\\'):
            return b'\\' + value[1:].capitalize()
        return value

    def __eq__(self, other) -> bool:
        if isinstance(other, Flag):
            return bytes(self) == bytes(other)
        elif isinstance(other, bytes):
            return bytes(self) == self._capitalize(other)
        return super().__eq__(other)

    def __lt__(self, other) -> bool:
        if isinstance(other, Flag):
            other_bytes = bytes(other)
        elif isinstance(other, bytes):
            other_bytes = self._capitalize(other)
        else:
            return NotImplemented
        if self.is_system and not other_bytes.startswith(b'\\'):
            return True
        elif not self.is_system and other_bytes.startswith(b'\\'):
            return False
        return bytes(self) < other_bytes

    def __hash__(self) -> int:
        return hash(bytes(self))

    def __repr__(self) -> str:
        return '<{0} value={1!r}>'.format(type(self).__name__, bytes(self))

    def __bytes__(self) -> bytes:
        return self.value

    @classmethod
    def parse(cls, buf: bytes, params: Params) -> Tuple['Flag', bytes]:
        try:
            _, buf = Space.parse(buf, params)
        except NotParseable:
            pass
        if buf:
            if buf[0] == 0x5c:
                atom, buf = Atom.parse(buf[1:], params)
                return cls(b'\\' + atom.value), buf
            else:
                atom, buf = Atom.parse(buf, params)
                return cls(atom.value), buf
        raise NotParseable(buf)


def get_system_flags() -> FrozenSet[Flag]:
    """Return the set of implemented system flags."""
    return frozenset({Seen, Recent, Deleted, Flagged, Answered, Draft})


#: The ``\\Seen`` system flag.
Seen = Flag(br'\Seen')

#: The ``\\Recent`` system flag.
Recent = Flag(br'\Recent')

#: The ``\\Deleted`` system flag.
Deleted = Flag(br'\Deleted')

#: The ``\\Flagged`` system flag.
Flagged = Flag(br'\Flagged')

#: The ``\\Answered`` system flag.
Answered = Flag(br'\Answered')

#: The ``\\Draft`` system flag.
Draft = Flag(br'\Draft')
