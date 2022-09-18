"""poetry-dotenv - is the tool that automatically loads environment variables from .env files."""

import os

import dotenv

from cleo.events.console_command_event import ConsoleCommandEvent
from cleo.events.console_events import COMMAND
from poetry.console.application import Application
from poetry.console.commands.env_command import EnvCommand
from poetry.plugins.application_plugin import ApplicationPlugin


class DotenvPlugin(ApplicationPlugin):
    """``poetry-dotenv`` - is the tool that automatically loads environment variables from ``.env``.

    ``poetry-dotenv`` - is the tool that automatically loads environment variables from ``.env``
    files into the environment before ``poetry`` commands are run.

    Notes
    -----
    To prevent ``poetry`` from loading the ``.env`` file, set the ``POETRY_DONT_LOAD_ENV``
    environment variable.

    If your ``.env`` file is located in a different path or has a different name you may set
    the ``POETRY_DOTENV_LOCATION`` environment variable.
    """

    def activate(self, application: Application) -> None:
        """Activate plugin."""

        application.event_dispatcher.add_listener(event_name=COMMAND, listener=self.load_dotenv)

    @staticmethod
    def load_dotenv(event: ConsoleCommandEvent, *args, **kwargs) -> None:
        """Load ``.env`` file."""

        if isinstance(event.command, EnvCommand) and not os.environ.get("POETRY_DONT_LOAD_DOTENV"):
            filepath = os.environ.get("POETRY_DOTENV_LOCATION") or dotenv.find_dotenv(usecwd=True)

            if event.io.is_debug():
                event.io.write_line(f"<debug>Loading environment variables {filepath!r}.</debug>")

            dotenv.load_dotenv(dotenv_path=filepath, override=True)
