"""Module that contains the core functionality of the plugin."""

import os

from cleo.events.console_command_event import ConsoleCommandEvent
from cleo.events.console_events import COMMAND
from poetry.console.application import Application
from poetry.console.commands.env_command import EnvCommand
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_dotenv import dotenv


class DotenvPlugin(ApplicationPlugin):
    """Plugin that automatically loads environment variables from dotenv files.

    Plugin that automatically loads environment variables from dotenv files into the environment
    before ``poetry`` commands are run.

    Notes
    -----
    To prevent ``poetry`` from loading the dotenv file, set the ``POETRY_DONT_LOAD_ENV``
    environment variable.

    If your dotenv file is located in a different path or has a different name you may set
    the ``POETRY_DOTENV_LOCATION`` environment variable.
    """

    def activate(self, application: Application) -> None:
        """Activate the plugin."""

        application.event_dispatcher.add_listener(  # pragma: no cover
            event_name=COMMAND,
            listener=self.load_dotenv,
        )

    @staticmethod
    def load_dotenv(event: ConsoleCommandEvent, *args, **kwargs) -> None:
        """Load the dotenv file."""

        dont_load_dotenv = os.getenv("POETRY_DONT_LOAD_DOTENV")
        dotenv_location = os.getenv("POETRY_DOTENV_LOCATION")

        if isinstance(event.command, EnvCommand) and not dont_load_dotenv:
            filepath = dotenv_location if dotenv_location else dotenv.find_dotenv(usecwd=True)

            if event.io.is_debug():
                event.io.write_line(f"<debug>Loading environment variables {filepath!r}.</debug>")

            dotenv.load_dotenv(dotenv_path=filepath, override=True)
