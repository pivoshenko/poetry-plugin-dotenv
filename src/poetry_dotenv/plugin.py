"""Module that contains the core functionality of the plugin."""

from cleo.events.console_command_event import ConsoleCommandEvent
from cleo.events.console_events import COMMAND
from poetry.console.application import Application
from poetry.plugins.application_plugin import ApplicationPlugin


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

    def activate(self, application: Application) -> None:
        """Activate the plugin."""

        application.event_dispatcher.add_listener(  # pragma: no cover
            event_name=COMMAND,
            listener=load_dotenv,
        )


def load_dotenv(event: ConsoleCommandEvent, *args, **kwargs) -> None:
    """Load a dotenv file."""
