"""Tests for the plugin."""

import os
import subprocess

from pathlib import Path


def test_with_default_dotenv_file(dotenv_content: str, dotenv_filepath: Path) -> None:
    """Test for the plugin with the default dotenv file location."""

    python_command = "import os; print(f'POSTGRES_USER={os.getenv(\"POSTGRES_USER\")}')"
    command = ["poetry", "run", "python", "-c", python_command]
    output = subprocess.run(command, capture_output=True).stdout.decode().strip()

    assert dotenv_content == output


def test_without_dotenv_file() -> None:
    """Test for the plugin without loading the dotenv file."""

    expected_output = "POSTGRES_USER=None"

    python_command = "import os; print(f'POSTGRES_USER={os.getenv(\"POSTGRES_USER\")}')"
    command = ["poetry", "run", "python", "-c", python_command]
    output = (
        subprocess.run(
            command,
            capture_output=True,
            env={"POETRY_DONT_LOAD_DOTENV": "1", **os.environ},
        )
        .stdout.decode()
        .strip()
    )
    assert expected_output == output
