"""Module that contains the core functionality of the plugin."""

from __future__ import annotations

import os
import enum

from typing import Self
from typing import TYPE_CHECKING

from cleo.events.console_events import COMMAND
from poetry.console.commands.env_command import EnvCommand
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_dotenv import config
from poetry_plugin_dotenv import dotenv


if TYPE_CHECKING:
    from cleo.events.console_command_event import ConsoleCommandEvent
    from poetry.console.application import Application


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

    def __init__(self: Self, event: ConsoleCommandEvent) -> None:
        """Initialize."""

        self.event = event

    def info(self: Self, msg: str) -> None:
        """Log a info message."""

        if self.event.io.is_debug():
            self.event.io.write_line(Verbosity.info.value.format(msg))

    def debug(self: Self, msg: str) -> None:
        """Log a debug message."""

        if self.event.io.is_debug():
            self.event.io.write_line(Verbosity.debug.value.format(msg))

    def warning(self: Self, msg: str) -> None:
        """Log a warning message."""

        if self.event.io.is_debug():
            self.event.io.write_line(Verbosity.warning.value.format(msg))

    def error(self: Self, msg: str) -> None:
        """Log a error message."""

        if self.event.io.is_debug():
            self.event.io.write_error_line(Verbosity.error.value.format(msg))


class DotenvPlugin(ApplicationPlugin):
    """Plugin that automatically loads environment variables from a dotenv file.

    Plugin that automatically loads environment variables from a dotenv file into the environment
    before ``poetry`` commands are run.
    """

    def activate(self: Self, application: Application) -> None:  # pragma: no cover
        """Activate the plugin."""

        application.event_dispatcher.add_listener(COMMAND, listener=self.load)  # type: ignore[union-attr, arg-type]

    def load(self: Self, event: ConsoleCommandEvent, *args, **kwargs) -> None:
        """Load a dotenv file."""

        logger = Logger(event)
        configuration = config.Config()

        is_env_command = isinstance(event.command, EnvCommand)

        if is_env_command and configuration.ignore:
            logger.warning("Not loading environment variables.")

        elif is_env_command and not configuration.ignore:
            filepath = (
                configuration.location if configuration.location else dotenv.core.find(usecwd=True)
            )

            if os.path.isfile(filepath):  # noqa: PTH113
                msg = f"Loading environment variables from '{filepath}'."
                logger.info(msg)
                dotenv.core.load(filepath=filepath)

            else:
                msg = f"File '{filepath}' doesn't exist."
                logger.error(msg)
