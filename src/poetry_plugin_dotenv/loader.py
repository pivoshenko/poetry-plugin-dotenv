"""Module that contains core loading functionality."""

from __future__ import annotations

import typing

from poetry_plugin_dotenv import dotenv


if typing.TYPE_CHECKING:  # pragma: no cover
    import pathlib

    from poetry_plugin_dotenv import configurator
    from poetry_plugin_dotenv import logging


def load(logger: logging.Logger, config: configurator.Config, working_dir: pathlib.Path) -> None:
    filepaths = _determine_filepaths(config, working_dir)

    if config.ignore:
        logger.warning("Not loading environment variables. Ignored by configuration")
        return

    if not filepaths:
        logger.warning("Not loading environment variables. No valid dotenv filepaths")
        return

    for filepath in filepaths:
        if filepath.is_file():
            logger.info(f"Loading environment variables: <fg=green>{filepath}</>")  # noqa: G004
            dotenv.core.load(filepath=filepath)
        else:
            logger.error(
                f"Could not load environment variables. The file does not exist: {filepath}"  # noqa: G004
            )


def _determine_filepaths(
    config: configurator.Config,
    working_dir: pathlib.Path,
) -> list[pathlib.Path]:
    if config.location:
        filepaths: list[pathlib.Path] = []

        for location_path in config.location:
            if location_path.is_absolute():
                filepaths.append(location_path.resolve())
            else:
                filepaths.append(working_dir / location_path)

        return filepaths

    filepath = dotenv.core.find(usecwd=True)
    return [filepath] if filepath else []
