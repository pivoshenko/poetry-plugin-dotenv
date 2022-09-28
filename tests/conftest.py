"""Fixtures and configuration for the tests."""

import os

from pathlib import Path
from typing import Callable
from typing import Dict

import pytest


@pytest.fixture()
def create_dotenv_file(tmp_path: Path) -> Callable[[str, str], Dict[str, str]]:
    """Get a dotenv file."""

    def create(user: str, filename: str) -> Dict[str, str]:
        """Create a dotenv file."""

        dotenv_content = {"POSTGRES_USER": user}
        dotenv_file = tmp_path / ".." / ".." / ".." / filename
        stream = (f"{env_key}={env_var}" for env_key, env_var in dotenv_content.items())
        dotenv_file.write_text("/n".join(stream))

        return dotenv_content

    return create


@pytest.fixture()
def remove_dotenv_file() -> Callable[[str], None]:
    """Remove a dotenv file."""

    def remove(filepath: str) -> None:
        """Remove a dotenv file."""

        os.unlink(filepath)

    return remove
