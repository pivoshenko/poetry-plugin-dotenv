"""Module that contains models for dotenv variables/literals."""

import re
import abc
import inspect

from typing import Any
from typing import Iterator
from typing import List
from typing import Mapping
from typing import Optional
from typing import Pattern


_posix_variable: Pattern[str] = re.compile(
    r"""
    \$\{
        (?P<name>[^\}:]*)
        (?::-
            (?P<default>[^\}]*)
        )?
    \}
    """,
    re.VERBOSE,
)


class Atom(abc.ABC, metaclass=abc.ABCMeta):
    """Base model for dotenv variables/literals."""

    def __repr__(self) -> str:
        """Get object representation."""

        attrs = self._get_attrs()
        attrs_vals = map(self._get_attr_value, attrs)

        pairs = map(lambda attr, attr_val: f"{attr!s}={attr_val!r}", attrs, attrs_vals)
        signature = ", ".join(pairs)

        # WPS237 - no need to use format-string here
        return f"{self.__class__.__name__!s}({signature!s})"  # noqa: WPS237

    def __str__(self) -> str:
        """Get string representation."""

        return self.__repr__()

    def __ne__(self, other: object) -> bool:
        """Implement not identity operator."""

        equal = self.__eq__(other)

        if equal is NotImplemented:
            return NotImplemented

        return not equal

    @abc.abstractmethod
    def resolve(self, *args, **kwargs) -> str:
        """Resolve a variable/literal."""

        raise NotImplementedError

    def _get_attrs(self) -> List[str]:
        """Get all attributes."""

        # WPS609 - init is necessary here to get signature
        signature = inspect.signature(self.__init__)  # type: ignore[misc]  # noqa: WPS609
        return [arg for arg in signature.parameters.keys() if arg != "self"]

    def _get_attr_value(self, attr: str) -> Any:
        """Get value of an attribute."""

        public = attr
        protected = f"_{attr}"
        # WPS237 - no need to use format-string here
        private = f"_{self.__class__.__name__}__{attr}"  # noqa: WPS237

        if public in self.__dict__:
            return self.__dict__.get(public)

        elif protected in self.__dict__:
            return self.__dict__.get(protected)

        elif private in self.__dict__:
            return self.__dict__.get(private)

        return None


class Literal(Atom):
    """Model of a dotenv literal."""

    def __init__(self, value: str) -> None:
        """Initialize."""

        self.value = value

    def __eq__(self, other: object) -> bool:
        """Implement identity operator."""

        if not isinstance(other, self.__class__):
            return NotImplemented

        return self.value == other.value

    def __hash__(self) -> int:
        """Get object hash."""

        return hash((self.__class__, self.value))

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
            return NotImplemented

        return (self.name, self.default) == (other.name, other.default)

    def __hash__(self) -> int:
        """Get object hash."""

        return hash((self.__class__, self.name, self.default))

    def resolve(self, env: Mapping[str, Optional[str]]) -> str:  # type: ignore[override]
        """Resolve a variable."""

        default = self.default if self.default is not None else ""
        env_val = env.get(self.name, default)
        return env_val if env_val is not None else ""


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
