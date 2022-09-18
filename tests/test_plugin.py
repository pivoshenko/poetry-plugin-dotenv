"""Tests for the plugin."""

import subprocess

from pathlib import Path


def test_with_default_dotenv_file(dotenv_content: str, dotenv_filepath: Path) -> None:
    """Test for the plugin with default ``.env`` file location."""

    python_command = "import os; print(f'POSTGRES_USER={os.getenv(\"POSTGRES_USER\")}')"
    output = (
        subprocess.run(["poetry", "run", "python", "-c", python_command], capture_output=True)
        .stdout.decode()
        .strip()
    )

    assert dotenv_content == output
