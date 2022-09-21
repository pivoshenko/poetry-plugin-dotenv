"""Fixtures and configuration for the tests."""

from pathlib import Path
from typing import Callable
from typing import Dict

import pytest


@pytest.fixture()
def crearte_dotenv_file(tmp_path: Path) -> Callable[[str, str], Dict[str, str]]:
    """Get the dotenv filepath and it's content."""

    def create(filename: str, user: str) -> Dict[str, str]:
        """Create dotenv file."""

        dotenv_content = {"POSTGRES_USER": user}
        dotenv_file = tmp_path / ".." / ".." / ".." / filename
        stream = (f"{env_key}={env_var}" for env_key, env_var in dotenv_content.items())
        dotenv_file.write_text("/n".join(stream))

        return dotenv_content

    return create
