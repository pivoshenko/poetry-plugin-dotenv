"""Module that contains dotenv parsers."""

from __future__ import annotations

import re
import codecs
import dataclasses

from typing import IO
from typing import TYPE_CHECKING

from poetry_plugin_dotenv.exceptions import PoetryPluginDotenvPatternError


if TYPE_CHECKING:  # pragma: no cover
    from collections.abc import Iterator


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


@dataclasses.dataclass(frozen=True)
class Original:
    """Represents the position of the original string in the file."""

    string: str
    line: int


@dataclasses.dataclass(frozen=True)
class Binding:
    """Represents a key-value pair from a dotenv file."""

    key: str | None
    value: str | None
    original: Original
    error: bool


@dataclasses.dataclass
class Position:
    """Model representing the cursor's position in the file."""

    chars: int
    line: int

    @classmethod
    def start(cls) -> Position:
        """Get the starting position (line 1, character 0)."""

        return cls(chars=0, line=1)

    def set(self, other: Position) -> None:
        """Set the current position to another position."""

        self.chars = other.chars
        self.line = other.line

    def advance(self, string: str) -> None:
        """Advance the position by the length of the given string."""

        self.chars += len(string)
        self.line += len(re.findall(_newline, string))


class Reader:
    """Reader for processing a dotenv file stream."""

    def __init__(self, stream: IO[str]) -> None:
        """Initialize the reader with a stream of data."""

        self.string = stream.read()
        self.position = Position.start()
        self.mark = Position.start()

    def has_next(self) -> bool:
        """Check if there are more characters to read."""

        return self.position.chars < len(self.string)

    def set_mark(self) -> None:
        """Set a mark at the current position."""

        self.mark.set(self.position)

    def get_marked(self) -> Original:
        """Get the portion of the string marked between the current position and the mark."""

        return Original(
            string=self.string[self.mark.chars : self.position.chars],
            line=self.mark.line,
        )

    def peek(self, count: int) -> str:
        """Peek ahead in the string without advancing the cursor."""

        return self.string[self.position.chars : self.position.chars + count]

    def read_regex(self, regex: re.Pattern[str]) -> tuple[str, ...]:
        """Match and read a portion of the string using the given regex."""

        match = regex.match(self.string, self.position.chars)

        if match is None:
            msg = "Pattern not found."
            raise PoetryPluginDotenvPatternError(msg)

        matched = self.string[match.start() : match.end()]
        self.position.advance(matched)
        return match.groups()


def decode_match(match: re.Match[str]) -> str:
    """Decode a match using unicode escapes."""

    return codecs.decode(match.group(0), "unicode-escape")


def decode_escapes(regex: re.Pattern[str], string: str) -> str:
    """Decode escape sequences in the string using the provided regex."""

    return regex.sub(decode_match, string)


def parse_key(reader: Reader) -> str | None:
    """Parse the key part of a dotenv binding."""

    char = reader.peek(1)

    if char == "#":
        return None

    if char == "'":
        (key,) = reader.read_regex(_single_quoted_key)

    else:
        (key,) = reader.read_regex(_unquoted_key)

    return key


def parse_unquoted_value(reader: Reader) -> str:
    """Parse a value that is not quoted."""

    (part,) = reader.read_regex(_unquoted_value)
    return re.sub(r"\s+#.*", "", part).rstrip()


def parse_value(reader: Reader) -> str:
    """Parse a value from a dotenv binding."""

    char = reader.peek(1)

    if char == "'":
        (value,) = reader.read_regex(_single_quoted_value)
        return decode_escapes(_single_quote_escapes, value)

    if char == '"':
        (value,) = reader.read_regex(_double_quoted_value)
        return decode_escapes(_double_quote_escapes, value)

    if char in {"", "\n", "\r"}:
        return ""

    return parse_unquoted_value(reader)


def parse_binding(reader: Reader) -> Binding:
    """Parse a single dotenv binding (key-value pair)."""

    reader.set_mark()

    try:
        reader.read_regex(_multiline_whitespace)

        if not reader.has_next():
            return Binding(key=None, value=None, original=reader.get_marked(), error=False)

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

        return Binding(key=key, value=value, original=reader.get_marked(), error=False)

    except PoetryPluginDotenvPatternError:
        reader.read_regex(_rest_of_line)
        return Binding(key=None, value=None, original=reader.get_marked(), error=True)


def parse_stream(stream: IO[str]) -> Iterator[Binding]:
    """Parse a dotenv stream and yield key-value bindings."""

    reader = Reader(stream)

    while reader.has_next():
        yield parse_binding(reader)
