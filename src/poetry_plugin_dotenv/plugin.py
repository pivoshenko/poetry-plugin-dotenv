"""Module that contains the core functionality of the plugin."""

from __future__ import annotations

import os

from typing import TYPE_CHECKING

from cleo.events.console_events import COMMAND
from poetry.console.commands.env_command import EnvCommand
from poetry.plugins.application_plugin import ApplicationPlugin

from poetry_plugin_dotenv import dotenv
from poetry_plugin_dotenv.config import Config
from poetry_plugin_dotenv.logger import Logger


if TYPE_CHECKING:  # pragma: no cover
    from cleo.events.console_command_event import ConsoleCommandEvent
    from poetry.console.application import Application


class DotenvPlugin(ApplicationPlugin):
    """Plugin that automatically loads environment variables from a dotenv file.

    Plugin that automatically loads environment variables from a dotenv file into the environment
    before ``poetry`` commands are run.
    """

    def activate(self, application: Application) -> None:  # pragma: no cover
        """Activate the plugin."""

        application.event_dispatcher.add_listener(COMMAND, listener=self.load)  # type: ignore[union-attr, arg-type]

    def load(self, event: ConsoleCommandEvent, *args, **kwargs) -> None:
        """Load a dotenv file."""

        logger = Logger(event)
        configuration = Config()

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
