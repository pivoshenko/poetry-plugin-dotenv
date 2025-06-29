"""Module that contains the core functionality of the plugin."""

from __future__ import annotations

from pathlib import Path
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

    Notes
    -----
    This plugin automatically loads environment variables from a dotenv file into the environment
    before the ``poetry`` commands are executed.

    """

    def activate(self, application: Application) -> None:  # pragma: no cover  # noqa: D102
        application.event_dispatcher.add_listener(COMMAND, listener=self.load)  # type: ignore[union-attr, arg-type]

    def load(self, event: ConsoleCommandEvent, *args, **kwargs) -> None:  # type: ignore[no-untyped-def]
        """Load a dotenv file according to the provided configuration."""

        directory_option = event.io.input.option("directory")
        working_dir = Path(directory_option) if directory_option else Path.cwd()

        logger = Logger(event)
        config = Config(working_dir)

        if not isinstance(event.command, EnvCommand):
            return  # pragma: nocover

        if config.ignore:
            logger.warning("Not loading environment variables. Ignored by configuration")
            return

        filepath = self._determine_filepath(config, working_dir)

        if not filepath:
            logger.warning("Not loading environment variables. No valid filepath")
            return

        if filepath.is_file():
            msg = f"Loading environment variables: <fg=green>{filepath}</>"
            logger.info(msg)
            dotenv.core.load(filepath)

        else:
            msg = f"Could not load environment variables. The file does not exist: {filepath}"
            logger.error(msg)

    def _determine_filepath(self, config: Config, working_dir: Path) -> Path | None:
        """Determine the appropriate filepath for the dotenv file."""

        if config.location and config.location != Path():
            location_path = config.location
            if location_path.is_absolute():
                return location_path.resolve()

            return working_dir / location_path

        return dotenv.core.find(usecwd=True)
