"""Module that contains custom commands."""

from __future__ import annotations

import os
import shutil
import typing
import pathlib

from poetry.console.commands.env_command import EnvCommand

from poetry_plugin_dotenv import configurator
from poetry_plugin_dotenv import loader
from poetry_plugin_dotenv import logging


if typing.TYPE_CHECKING:  # pragma: no cover
    from poetry.utils.env import Env


def activate_command_factory() -> ActivateCommand:  # pragma: no cover
    return ActivateCommand()


class ActivateCommand(EnvCommand):
    """Command that loads dotenv variables and activates the virtual environment."""

    name = "activate"
    description = (
        "Load environment variables from dotenv file and activate the virtual environment."
    )

    def handle(self) -> int:  # pragma: no cover
        directory_option = self.option("directory")
        working_dir = pathlib.Path(directory_option) if directory_option else pathlib.Path.cwd()

        logger = logging.Logger(self)  # type: ignore[arg-type]
        config = configurator.Config(working_dir)

        activation_command = self._get_venv_activation_command(self.env)
        if not activation_command:
            logger.error("Failed to identify the activation command.")
            return 1

        loader.load(logger, config, working_dir)

        shell = os.environ.get("SHELL", "")
        if not shell:
            # Detect PowerShell by presence of PSMODULEPATH or executable on PATH
            pwsh_present = (
                os.environ.get("PSMODULEPATH") is not None
                or shutil.which("pwsh")
                or shutil.which("powershell")
            )
            if pwsh_present:
                ps_exe = shutil.which("pwsh") or shutil.which("powershell")
                if ps_exe:
                    # Run PowerShell, execute activation command and keep interactive session
                    os.execvp(ps_exe, [ps_exe, "-NoExit", "-Command", activation_command])  # noqa: S606

                # If PowerShell isn't available, try cmd.exe (COMSPEC)
                comspec = os.environ.get("COMSPEC") or shutil.which("cmd")
                if comspec:
                    os.execvp(comspec, [comspec, "/k", activation_command])  # noqa: S606

        # Fallback to POSIX-like shells
        shell = shell or "/bin/bash"
        os.execvp(shell, [shell, "-c", f"{activation_command}; exec {shell}"])  # noqa: S606

        return 0

    def _get_venv_activation_command(self, venv: Env) -> str | None:  # pragma: no cover
        shell = os.environ.get("SHELL", "")

        if "fish" in shell:
            activate_script = venv.path / "bin" / "activate.fish"
            if activate_script.exists():
                return f"source {activate_script}"
            return None

        activate_script = venv.path / "bin" / "activate"
        if activate_script.exists():
            return f"source {activate_script}"

        # Windows: virtualenv uses Scripts\Activate.ps1 (PowerShell) or activate.bat (cmd)
        if os.name == "nt" or not shell:
            ps1 = venv.path / "Scripts" / "Activate.ps1"
            if ps1.exists():
                # Use PowerShell command to dot-source the script so variables export to session
                return f"& '{ps1}'"

            bat = venv.path / "Scripts" / "activate.bat"
            if bat.exists():
                # Return path to batch file; the caller can invoke cmd.exe /k <bat>
                return str(bat)

        return None
