"""Module that contains the core functionality of the plugin."""

import os

from cleo.events.console_command_event import ConsoleCommandEvent
from cleo.events.console_events import COMMAND
from poetry.console.application import Application
from poetry.console.commands.env_command import EnvCommand
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_dotenv import dotenv


class DotenvPlugin(ApplicationPlugin):
    """Plugin that automatically loads environment variables from a dotenv file.

    Plugin that automatically loads environment variables from a dotenv file into the environment
    before ``poetry`` commands are run.

    Notes
    -----
    To prevent ``poetry`` from loading the dotenv file, set the ``POETRY_DONT_LOAD_ENV``
    environment variable.

    If your dotenv file is located in a different path or has a different name you may set
    the ``POETRY_DOTENV_LOCATION`` environment variable.
    """

    debug_msg = "<debug>{0!s}</debug>"

    def activate(self, application: Application) -> None:
        """Activate the plugin."""

        application.event_dispatcher.add_listener(  # pragma: no cover
            event_name=COMMAND,
            listener=self.load,
        )

    def debug(self, event: ConsoleCommandEvent, message: str) -> None:  # pragma: no cover
        """Log a debug message."""

        if event.io.is_debug():
            event.io.write_line(self.debug_msg.format(message))

    def load(self, event: ConsoleCommandEvent, *args, **kwargs) -> None:
        """Load a dotenv file."""

        dont_load_dotenv = os.getenv("POETRY_DONT_LOAD_DOTENV")
        dotenv_location = os.getenv("POETRY_DOTENV_LOCATION")
        is_env_command = isinstance(event.command, EnvCommand)

        if is_env_command and dont_load_dotenv:
            self.debug(event, "Not loading environment variables.")

        elif is_env_command and not dont_load_dotenv:
            filepath = dotenv_location if dotenv_location else dotenv.core.find(usecwd=True)

            if os.path.isfile(filepath):
                self.debug(event, "Loading environment variables from {0!r}.".format(filepath))
                dotenv.core.load(filepath=filepath)

            else:
                self.debug(event, "File {0!r} doesn't exist.".format(filepath))
