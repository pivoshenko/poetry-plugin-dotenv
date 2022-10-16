"""Module that contains models of the dotenv variables/literals."""

from __future__ import annotations

import re
import abc

from typing import Iterator
from typing import OrderedDict


_posix_variable = re.compile(
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
    """Base model."""

    def __repr__(self) -> str:
        """Get object representation."""

        fields = tuple(self.__dict__.items())

        signature_parts = ("{0!s}={1!r}".format(*pair) for pair in fields)
        signature = ", ".join(signature_parts)

        return "{class_name!s}({signature!s})".format(
            class_name=self.__class__.__name__,
            signature=signature,
        )

    def __str__(self) -> str:
        """Get string representation."""

        return self.__repr__()

    @abc.abstractmethod
    def resolve(self, *args, **kwargs) -> str:  # pragma: no cover
        """Resolve."""

        raise NotImplementedError


class Literal(Atom):
    """Model of a literal."""

    def __init__(self, value: str) -> None:
        """Initialize."""

        self.value = value

    def __eq__(self, other: object) -> bool:
        """Compare objects."""

        if isinstance(other, Literal):
            return self.value == other.value

        raise TypeError("Invalid type: {0!r}.".format(type(other)))

    def __hash__(self) -> int:
        """Get object hash."""

        return hash((self.__class__.__name__, self.value))

    def resolve(self, *args, **kwargs) -> str:
        """Get a literal value."""

        return self.value


class Variable(Atom):
    """Model of a variable."""

    def __init__(self, name: str, default: str | None = None) -> None:
        """Initialize."""

        self.name = name
        self.default = default

    def __eq__(self, other: object) -> bool:
        """Compare objects."""

        if isinstance(other, Variable):
            return (self.name, self.default) == (other.name, other.default)

        raise TypeError("Invalid type: {0!r}.".format(type(other)))

    def __hash__(self) -> int:
        """Get object hash."""

        return hash((self.__class__.__name__, self.name, self.default))

    def resolve(self, env: OrderedDict[str, str | None]) -> str:
        """Get a variable value."""

        default = self.default if self.default else ""
        env_val = env.get(self.name, default)
        return env_val if env_val else ""


def parse(value: str) -> Iterator[Atom]:
    """Parse values."""

    cursor = 0

    for match in _posix_variable.finditer(value):
        start, end = match.span()
        name = match.groupdict()["name"]
        default = match.groupdict()["default"]

        if start > cursor:
            yield Literal(value=value[cursor:start])

        yield Variable(name=name, default=default)
        cursor = end

    length = len(value)
    if cursor < length:
        yield Literal(value=value[cursor:length])
