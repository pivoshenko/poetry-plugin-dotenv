"""Module that contains models for dotenv variables/literals."""

import re
import abc

from typing import Iterator
from typing import Mapping
from typing import Optional
from typing import Pattern


_posix_variable: Pattern[str] = re.compile(
    r"""
    \$\{
        (?P<name>[^}:]*)
        (?::-
            (?P<default>[^}]*)
        )?
    }
    """,
    re.VERBOSE,
)


class Atom(abc.ABC, metaclass=abc.ABCMeta):
    """Base model for dotenv variables/literals."""

    def __repr__(self) -> str:
        """Get object representation."""

        fields = tuple(self.__dict__.items())

        signature_parts = ("{0!s}={1!r}".format(*pair) for pair in fields)
        signature = ", ".join(signature_parts)

        # WPS237 - no need to use format-string here
        return f"{self.__class__.__name__!s}({signature!s})"  # noqa: WPS237

    def __str__(self) -> str:
        """Get string representation."""

        return self.__repr__()

    @abc.abstractmethod
    def resolve(self, *args, **kwargs) -> str:
        """Resolve a variable/literal."""

        raise NotImplementedError  # pragma: no cover


class Literal(Atom):
    """Model of a dotenv literal."""

    def __init__(self, value: str) -> None:
        """Initialize."""

        self.value = value

    def __eq__(self, other: object) -> bool:
        """Implement identity operator."""

        if not isinstance(other, self.__class__):
            raise NotImplemented  # pragma: no cover

        return self.value == other.value

    def __hash__(self) -> int:
        """Get object hash."""

        return hash((self.__class__, self.value))  # pragma: no cover

    def resolve(self, *args, **kwargs) -> str:
        """Resolve a literal."""

        return self.value


class Variable(Atom):
    """Model of a dotenv variable."""

    def __init__(self, name: str, default: Optional[str]) -> None:
        """Initialize."""

        self.name = name
        self.default = default

    def __eq__(self, other: object) -> bool:
        """Implement identity operator."""

        if not isinstance(other, self.__class__):
            raise NotImplemented  # pragma: no cover

        return (self.name, self.default) == (other.name, other.default)

    def __hash__(self) -> int:
        """Get object hash."""

        return hash((self.__class__, self.name, self.default))  # pragma: no cover

    def resolve(self, env: Mapping[str, Optional[str]]) -> str:  # type: ignore[override]
        """Resolve a variable."""

        default = self.default if self.default is not None else ""  # pragma: no cover
        env_val = env.get(self.name, default)  # pragma: no cover
        return env_val if env_val is not None else ""  # pragma: no cover


def parse_variables(value: str) -> Iterator[Atom]:
    """Parse dotenv variables."""

    cursor = 0

    for match in _posix_variable.finditer(value):
        (start, end) = match.span()
        name = match.groupdict()["name"]
        default = match.groupdict()["default"]

        if start > cursor:
            yield Literal(value=value[cursor:start])

        yield Variable(name=name, default=default)
        cursor = end

    length = len(value)
    if cursor < length:
        yield Literal(value=value[cursor:length])
