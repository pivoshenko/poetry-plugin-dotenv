"""Module that contains models of the dotenv variables/literals."""

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
    """Model of a literal."""

    value: str

    def resolve(self, *args, **kwargs) -> str:  # type: ignore[no-untyped-def]
        """Get a literal value."""

        return self.value


@dataclasses.dataclass(frozen=True)
class Variable:
    """Model of a variable."""

    name: str
    default: str | None = None

    def resolve(self, env: OrderedDict[str, str], *args, **kwargs) -> str:  # type: ignore[no-untyped-def]
        """Get a variable value."""

        default = self.default if self.default else ""
        env_val = env.get(self.name, default)
        return env_val if env_val else ""


def parse(value: str) -> Iterator[Literal | Variable]:
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
