"""Module that contains logging functionality."""

from __future__ import annotations

import enum
import typing
import functools

from cleo.io.outputs.output import Verbosity


if typing.TYPE_CHECKING:  # pragma: no cover
    from cleo.events.console_command_event import ConsoleCommandEvent


class LoggingStyle(enum.Enum):
    """Style tags to color text output."""

    INFO = "<info>{0!s}</info>"
    DEBUG = "<debug>{0!s}</debug>"
    WARNING = "<warning>{0!s}</warning>"
    ERROR = "<error>{0!s}</error>"

    def __call__(self, text: str) -> str:
        return self.value.format(text)


class Logger:
    """Logger for the ``poetry`` events.

    Notes
    -----
    Since this logger is used by a plugin that runs before the main command,
    all messages are logged only in debug mode.

    """

    def __init__(self, event: ConsoleCommandEvent) -> None:
        self.write_line = functools.partial(
            event.io.write_line,
            verbosity=Verbosity.VERBOSE,
        )

    def info(self, msg: str) -> None:
        self._log(LoggingStyle.INFO, msg)

    def warning(self, msg: str) -> None:
        self._log(LoggingStyle.WARNING, msg)

    def error(self, msg: str) -> None:  # pragma: no cover
        self._log(LoggingStyle.ERROR, msg)

    def _log(self, style: LoggingStyle, msg: str) -> None:
        self.write_line(style(msg))
