"""Module that contains the core functionality of the plugin."""

import os
import enum

from cleo.events.console_command_event import ConsoleCommandEvent
from cleo.events.console_events import COMMAND
from poetry.console.application import Application
from poetry.console.commands.env_command import EnvCommand
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_dotenv import dotenv


class Verbosity(enum.Enum):  # pragma: no cover
    """Levels of verbosity."""

    info: str = "<info>{0!s}</info>"
    debug: str = "<debug>{0!s}</debug>"
    warning: str = "<warning>{0!s}</warning>"
    error: str = "<error>{0!s}</error>"


class Logger(object):  # pragma: no cover
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


class DotenvPlugin(ApplicationPlugin):
    """Plugin that automatically loads environment variables from a dotenv file.

    Plugin that automatically loads environment variables from a dotenv file into the environment
    before ``poetry`` commands are run.

    Notes
    -----
    To prevent ``poetry`` from loading the dotenv file, set the ``POETRY_DONT_LOAD_DOTENV``
    environment variable.

    If your dotenv file is located in a different path or has a different name you may set
    the ``POETRY_DOTENV_LOCATION`` environment variable.
    """

    def activate(self, application: Application) -> None:  # pragma: no cover
        """Activate the plugin."""

        application.event_dispatcher.add_listener(
            event_name=COMMAND,
            listener=self.load,
        )

    def load(self, event: ConsoleCommandEvent, *args, **kwargs) -> None:
        """Load a dotenv file."""

        logger = Logger(event)

        dont_load_dotenv = os.getenv("POETRY_DONT_LOAD_DOTENV")
        dotenv_location = os.getenv("POETRY_DOTENV_LOCATION")
        is_env_command = isinstance(event.command, EnvCommand)

        if is_env_command and dont_load_dotenv:
            logger.warning("Not loading environment variables.")

        elif is_env_command and not dont_load_dotenv:
            filepath = dotenv_location if dotenv_location else dotenv.core.find(usecwd=True)

            if os.path.isfile(filepath):
                logger.info("Loading environment variables from {0!r}.".format(filepath))
                dotenv.core.load(filepath=filepath)

            else:
                logger.error("File {0!r} doesn't exist.".format(filepath))
