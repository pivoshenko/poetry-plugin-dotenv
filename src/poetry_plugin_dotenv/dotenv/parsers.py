"""Module that contains dotenv parsers."""

from __future__ import annotations

import re
import codecs
import dataclasses

from typing import IO
from typing import NamedTuple
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from collections.abc import Iterator


class Original(NamedTuple):
    """Position of the original string in the file."""

    string: str
    line: int


class Binding(NamedTuple):
    """Binding of a key and a value."""

    key: str | None
    value: str | None
    original: Original
    error: bool


class DotenvParseError(Exception):
    """Exception for dotenv parse errors."""


def make_regex(string: str, extra_flags: int = 0) -> re.Pattern[str]:
    """Construct a regex expression."""

    return re.compile(string, re.UNICODE | extra_flags)


_newline = make_regex(r"(\r\n|\n|\r)")
_multiline_whitespace = make_regex(r"\s*", extra_flags=re.MULTILINE)
_whitespace = make_regex(r"[^\S\r\n]*")
_export = make_regex(r"(?:export[^\S\r\n]+)?")
_single_quoted_key = make_regex("'([^']+)'")
_unquoted_key = make_regex(r"([^=\#\s]+)")
_equal_sign = make_regex(r"(=[^\S\r\n]*)")
_single_quoted_value = make_regex(r"'((?:\\'|[^'])*)'")
_double_quoted_value = make_regex(r'"((?:\\"|[^"])*)"')
_unquoted_value = make_regex(r"([^\r\n]*)")
_comment = make_regex(r"(?:[^\S\r\n]*#[^\r\n]*)?")
_end_of_line = make_regex(r"[^\S\r\n]*(?:\r\n|\n|\r|$)")
_rest_of_line = make_regex(r"[^\r\n]*(?:\r|\n|\r\n)?")
_double_quote_escapes = make_regex(r"\\[\\'\"abfnrtv]")
_single_quote_escapes = make_regex(r"\\[\\']")


@dataclasses.dataclass
class Position:
    """Model of a cursor position."""

    chars: int
    line: int

    @classmethod
    def start(cls) -> Position:
        """Get a start position."""

        return cls(chars=0, line=1)

    def set(self, other: Position) -> None:  # noqa: A003
        """Set a position."""

        self.chars = other.chars
        self.line = other.line

    def advance(self, string: str) -> None:
        """Update a position."""

        self.chars += len(string)
        self.line += len(re.findall(_newline, string))


class Reader:
    """Dotenv reader."""

    def __init__(self, stream: IO[str]) -> None:
        """Initialize."""

        self.string = stream.read()
        self.position = Position.start()
        self.mark = Position.start()

    def has_next(self) -> bool:
        """Check if a dotenv has the next position."""

        return self.position.chars < len(self.string)

    def set_mark(self) -> None:
        """Set a mark."""

        self.mark.set(self.position)

    def get_marked(self) -> Original:
        """Get a mark."""

        # fmt: off
        return Original(
            string=self.string[self.mark.chars: self.position.chars],
            line=self.mark.line,
        )
        # fmt: on

    def peek(self, count: int) -> str:
        """Peek a dotenv."""

        # fmt: off
        return self.string[self.position.chars: self.position.chars + count]
        # fmt: on

    def read_regex(self, regex: re.Pattern[str]) -> tuple[str, ...]:
        """Read a dotenv with a regex."""

        match = regex.match(self.string, self.position.chars)

        if match is None:
            msg = "Pattern not found."
            raise DotenvParseError(msg)

        # fmt: off
        matched = self.string[match.start(): match.end()]
        # fmt: on

        self.position.advance(matched)
        return match.groups()


def decode_match(match: re.Match[str]) -> str:
    """Decode matches."""

    return codecs.decode(match.group(0), "unicode-escape")


def decode_escapes(regex: re.Pattern[str], string: str) -> str:
    """Decode escape symbols."""

    return regex.sub(decode_match, string)


def parse_key(reader: Reader) -> str | None:
    """Parse a dotenv key."""

    char = reader.peek(1)

    if char == "#":
        return None

    elif char == "'":  # noqa: RET505
        key, *_ = reader.read_regex(_single_quoted_key)

    else:
        key, *_ = reader.read_regex(_unquoted_key)

    return key


def parse_unquoted_value(reader: Reader) -> str:
    """Parse an unquoted dotenv value."""

    part, *_ = reader.read_regex(_unquoted_value)
    return re.sub(r"\s+#.*", "", part).rstrip()


def parse_value(reader: Reader) -> str:
    """Parse a dotenv value."""

    char = reader.peek(1)

    if char == "'":
        value, *_ = reader.read_regex(_single_quoted_value)
        return decode_escapes(_single_quote_escapes, value)

    elif char == '"':  # noqa: RET505
        value, *_ = reader.read_regex(_double_quoted_value)
        return decode_escapes(_double_quote_escapes, value)

    elif char in {"", "\n", "\r"}:
        return ""

    return parse_unquoted_value(reader)


def parse_binding(reader: Reader) -> Binding:
    """Parse a dotenv binding."""

    reader.set_mark()

    try:
        reader.read_regex(_multiline_whitespace)

        if not reader.has_next():
            return Binding(
                key=None,
                value=None,
                original=reader.get_marked(),
                error=False,
            )

        reader.read_regex(_export)
        key = parse_key(reader)
        reader.read_regex(_whitespace)

        if reader.peek(1) == "=":
            reader.read_regex(_equal_sign)
            value = parse_value(reader)

        else:
            value = None

        reader.read_regex(_comment)
        reader.read_regex(_end_of_line)

        return Binding(
            key=key,
            value=value,
            original=reader.get_marked(),
            error=False,
        )

    except DotenvParseError:
        reader.read_regex(_rest_of_line)
        return Binding(
            key=None,
            value=None,
            original=reader.get_marked(),
            error=True,
        )


def parse_stream(stream: IO[str]) -> Iterator[Binding]:
    """Parse a dotenv stream."""

    reader = Reader(stream)

    while reader.has_next():
        yield parse_binding(reader)
