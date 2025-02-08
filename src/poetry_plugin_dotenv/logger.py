"""Module that contains plugin's logger."""

from __future__ import annotations

import enum

from functools import partial
from typing import TYPE_CHECKING

from cleo.io.outputs.output import Verbosity


if TYPE_CHECKING:  # pragma: no cover
    from cleo.events.console_command_event import ConsoleCommandEvent


class Style(enum.Enum):
    """Style tags to color text output."""

    INFO = "<info>{0!s}</info>"
    DEBUG = "<debug>{0!s}</debug>"
    WARNING = "<warning>{0!s}</warning>"
    ERROR = "<error>{0!s}</error>"

    def __call__(self, text: str) -> str:
        """Apply the style to the text."""

        return self.value.format(text)


class Logger:
    """Logger for the ``poetry`` events.

    Notes
    -----
    Since this logger is used by a plugin that runs before the main command,
    all messages are logged only in debug mode.

    """

    def __init__(self, event: ConsoleCommandEvent) -> None:
        """Initialize the logger."""

        self.write_line = partial(event.io.write_line, verbosity=Verbosity.DEBUG)

    def info(self, msg: str) -> None:
        """Log an informational message."""

        self._log(Style.INFO, msg)

    def debug(self, msg: str) -> None:
        """Log a debug message."""

        self._log(Style.DEBUG, msg)  # pragma: nocover

    def warning(self, msg: str) -> None:
        """Log a warning message."""

        self._log(Style.WARNING, msg)

    def error(self, msg: str) -> None:
        """Log an error message."""

        self._log(Style.ERROR, msg)

    def _log(self, style: Style, msg: str) -> None:
        """Log a message with the given style."""

        self.write_line(style(msg))
