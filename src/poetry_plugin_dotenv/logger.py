"""Module that contains plugin's logger."""

from __future__ import annotations

import enum

from functools import partial
from typing import TYPE_CHECKING

from cleo.io.outputs.output import Verbosity


if TYPE_CHECKING:  # pragma: no cover
    from cleo.events.console_command_event import ConsoleCommandEvent


class Style(enum.Enum):  # pragma: no cover
    """Style tags to color text output."""

    info = "<info>{0!s}</info>"
    debug = "<debug>{0!s}</debug>"
    warning = "<warning>{0!s}</warning>"
    error = "<error>{0!s}</error>"

    def __call__(self, text: str) -> str:
        """Apply a style to the text."""

        return self.value.format(text)


class Logger:  # pragma: no cover
    """Logger of the ``poetry`` events.

    Notes
    -----
    Because this logger is used for the plugin that are running before the main command,
    all the messages will be logged only in the debug mode.

    """

    def __init__(self, event: ConsoleCommandEvent) -> None:
        """Initialize."""

        self.event = event
        self.write_line = partial(event.io.write_line, verbosity=Verbosity.DEBUG)

    def info(self, msg: str) -> None:
        """Log a info message."""

        self.write_line(Style.info(msg))

    def debug(self, msg: str) -> None:
        """Log a debug message."""

        self.write_line(Style.debug(msg))

    def warning(self, msg: str) -> None:
        """Log a warning message."""

        self.write_line(Style.warning(msg))

    def error(self, msg: str) -> None:
        """Log a error message."""

        self.write_line(Style.error(msg))
