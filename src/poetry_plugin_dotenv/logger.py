"""Module that contains plugin logger."""

from __future__ import annotations

import enum

from typing import TYPE_CHECKING


if TYPE_CHECKING:  # pragma: no cover
    from cleo.events.console_command_event import ConsoleCommandEvent


class Verbosity(enum.Enum):  # pragma: no cover
    """Levels of verbosity."""

    info = "<info>{0!s}</info>"
    debug = "<debug>{0!s}</debug>"
    warning = "<warning>{0!s}</warning>"
    error = "<error>{0!s}</error>"


class Logger:  # pragma: no cover
    """Logger of the ``poetry`` events.

    Because this logger is used for the plugin that are running before the main command,
    all the messages will be logged only in the debug mode.
    """

    def __init__(self, event: ConsoleCommandEvent) -> None:
        """Initialize."""

        self.event = event

    def info(self, msg: str) -> None:
        """Log a info message."""

        if self.event.io.is_debug():
            self.event.io.write_line(Verbosity.info.value.format(msg))

    def debug(self, msg: str) -> None:
        """Log a debug message."""

        if self.event.io.is_debug():
            self.event.io.write_line(Verbosity.debug.value.format(msg))

    def warning(self, msg: str) -> None:
        """Log a warning message."""

        if self.event.io.is_debug():
            self.event.io.write_line(Verbosity.warning.value.format(msg))

    def error(self, msg: str) -> None:
        """Log a error message."""

        if self.event.io.is_debug():
            self.event.io.write_error_line(Verbosity.error.value.format(msg))
