"""Module that contains models of the dotenv variables/literals."""

from __future__ import annotations

import re
import typing
import dataclasses


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


@dataclasses.dataclass(frozen=True)
class Literal:
    """Model of a literal."""

    value: str

    def resolve(self, *args, **kwargs) -> str:
        """Get a literal value."""

        return self.value


@dataclasses.dataclass(frozen=True)
class Variable:
    """Model of a variable."""

    name: str
    default: str | None = None

    def resolve(self, env: typing.OrderedDict[str, str], *args, **kwargs) -> str:
        """Get a variable value."""

        default = self.default if self.default else ""
        env_val = env.get(self.name, default)
        return env_val if env_val else ""


def parse(value: str) -> typing.Iterator[Literal | Variable]:
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
