"""Module that contains plugin configuration."""

from __future__ import annotations

import os
import dataclasses

from pathlib import Path

import tomlkit


CONFIG_SOURCES: dict[str, str] = {
    "pyproject.toml": "tool.poetry.plugins.dotenv",
    "os": "POETRY_PLUGIN_DOTENV_",
}

_STR_BOOLEAN_MAPPING: dict[str, bool] = {
    "y": True,
    "yes": True,
    "t": True,
    "on": True,
    "1": True,
    "true": True,
    "n": False,
    "no": False,
    "f": False,
    "off": False,
    "0": False,
    "false": False,
}


@dataclasses.dataclass
class _Config:
    """Defines the data schema and defaults used for plugin configuration."""

    ignore: bool = False
    location: str | None = None


# TODO(pivoshenko): this configuration loader is a "quick patch" solution
class Config(_Config):
    """Configuration loader."""

    def __init__(self) -> None:
        """Initialize."""

        source_config = {}
        for config_source, section in CONFIG_SOURCES.items():
            if config_source.endswith(".toml"):
                config = _load_config_from_toml(config_source, section)

            elif config_source.endswith("os"):
                config = _load_config_from_os(section)

            else:  # pragma: no cover
                pass

            source_config.update(config)

        for attribute in self.__dataclass_fields__:
            default_attribute_value: bool | str | None = self.__getattribute__(attribute)
            source_attribute_value = source_config.get(attribute)

            # fmt: off
            if (
                isinstance(default_attribute_value, bool)
                and not isinstance(source_attribute_value, bool)
                and source_attribute_value
            ):
                source_attribute_value = _as_bool(source_attribute_value)
            # fmt: on

            if source_attribute_value:
                self.__setattr__(attribute, source_attribute_value)


def _load_config_from_toml(
    filename: str,
    section: str,
) -> dict[str, str | bool | None]:
    """Load configuration from the TOML file."""

    filepath = Path(filename)

    if filepath.exists():
        with filepath.open("rb") as toml_file:
            toml = tomlkit.load(toml_file)

        config = toml
        for key in section.split("."):
            config = config.get(key, {})

        return config

    return {}  # pragma: no cover


def _load_config_from_os(
    section: str,
) -> dict[str, str | bool | None]:
    """Load configuration from the OS environment variables."""

    return {
        key.replace(section, "").lower(): value
        for key, value in os.environ.items()
        if key.startswith(section)
    }


def _as_bool(value: str) -> bool:
    """Given a string value that represents True or False, returns the Boolean equivalent.

    Heavily inspired from ``distutils strtobool``.
    """

    try:
        return _STR_BOOLEAN_MAPPING[value.lower()]

    except KeyError:
        msg = f"Invalid truth value {value}"
        raise ValueError(msg) from None
