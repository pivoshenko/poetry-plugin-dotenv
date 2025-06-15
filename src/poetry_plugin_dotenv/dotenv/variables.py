"""Module that contains models of the dotenv variables and literals."""

from __future__ import annotations

import re
import dataclasses

from typing import TYPE_CHECKING


if TYPE_CHECKING:  # pragma: no cover
    from collections import OrderedDict
    from collections.abc import Iterator


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
    """Represents a literal value."""

    value: str

    def resolve(self, *args, **kwargs) -> str:  # type: ignore[no-untyped-def]
        """Get a literal value."""

        return self.value


@dataclasses.dataclass(frozen=True)
class Variable:
    """Represents a variable with an optional default value."""

    name: str
    default: str | None = None

    def resolve(self, env: OrderedDict[str, str], *args, **kwargs) -> str:  # type: ignore[no-untyped-def]
        """Resolve the variable value from the environment or use the default."""

        return env.get(self.name, self.default) or ""  # type: ignore[arg-type]


def parse(value: str) -> Iterator[Literal | Variable]:
    """Parse a string and yield literals and variables."""

    cursor = 0
    value_length = len(value)
    matches = list(_posix_variable.finditer(value))

    for match in matches:
        start, end = match.span()
        name = match.group("name")
        default = match.group("default")

        if start > cursor:
            yield Literal(value=value[cursor:start])

        yield Variable(name=name, default=default)
        cursor = end

    if cursor < value_length:
        yield Literal(value=value[cursor:])
