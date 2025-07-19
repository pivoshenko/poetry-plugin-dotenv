"""Module that contains core loading functionality."""

from __future__ import annotations

import typing
import pathlib

from poetry_plugin_dotenv import dotenv


if typing.TYPE_CHECKING:  # pragma: no cover
    from poetry_plugin_dotenv import configurator
    from poetry_plugin_dotenv import logging


def load(logger: logging.Logger, config: configurator.Config, working_dir: pathlib.Path) -> None:
    filepath = _determine_filepath(config, working_dir)

    if config.ignore:
        logger.warning("Not loading environment variables. Ignored by configuration")
        return

    if not filepath:
        logger.warning("Not loading environment variables. No valid filepath")
        return

    if filepath.is_file():
        logger.info(f"Loading environment variables: <fg=green>{filepath}</>")  # noqa: G004
        dotenv.core.load(filepath=filepath)
    else:
        logger.error(f"Could not load environment variables. The file does not exist: {filepath}")  # noqa: G004


def _determine_filepath(
    config: configurator.Config,
    working_dir: pathlib.Path,
) -> pathlib.Path | None:
    if config.location and config.location != pathlib.Path():
        location_path = config.location
        if location_path.is_absolute():
            return location_path.resolve()

        return working_dir / location_path

    return dotenv.core.find(usecwd=True)
