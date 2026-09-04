# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Poetry **application plugin** (entry point `poetry.application.plugin` -> `poetry_plugin_dotenv.plugin:DotenvPlugin` in `pyproject.toml`) that loads a dotenv file into `os.environ` before any `poetry` command runs, and adds a `poetry activate` command that re-execs the user's shell with the venv activated and dotenv variables loaded.

Hard constraints that shape the code:

- Must support `poetry >=1.5,<3` and Python `>=3.9,<4` (`~=3.9,<4.0` in `pyproject.toml`).
- **No runtime dependencies beyond `poetry` itself.** `src/poetry_plugin_dotenv/dotenv/` is a vendored fork of `python-dotenv` precisely to keep it that way — do not add `python-dotenv` or any other runtime dependency.

## Commands

`just` is the entry point for every task (`justfile`); CI runs the same recipes. Note the split: formatters/linters run via `uvx` (uv-managed, outside the venv), tests via `poetry run`.

- `just install` — `poetry install --all-groups --all-extras` (venv is in-project: `poetry.toml` sets `virtualenvs.in-project = true`)
- `just format` — `uvx pyupgrade --py310-plus` over all `.py`, then `uvx ruff check --fix .`, then `uvx ruff format .`
- `just lint` — `uvx ruff check .` then `uvx ty check`
- `just test` — `poetry run pytest` (skipped if a `.no-tests` sentinel file exists at repo root; none is committed)
- `just check` — lint + test
- `just audit` — `uvx pip-audit`
- `just update` — `poetry update`

Single test: `poetry run pytest tests/test_plugin.py::test_default_dotenv_file` or `poetry run pytest -k <pattern>`.

CI (`.github/workflows/ci.yaml`) gates on `just lint`, `just audit`, `just test` (Python 3.13, ubuntu ARM).

## Architecture

Per-command flow (`src/poetry_plugin_dotenv/`):

1. `plugin.DotenvPlugin.activate` registers `load` as a listener on cleo's `COMMAND` event and registers the `activate` command factory. Commands in `plugin.COMMANDS_EXCLUSION` (`{"activate"}`) are skipped — `ActivateCommand` does its own loading.
2. `plugin.load` resolves `working_dir` from the `--directory` option (else cwd), builds `logging.Logger(event)` and `configurator.Config(working_dir)`, and calls `loader.load`.
3. `configurator.Config` iterates `CONFIG_SOURCES` in order — `[tool.poetry.plugins.dotenv]`, then `[tool.dotenv]` (both in the project's `pyproject.toml`), then `POETRY_PLUGIN_DOTENV_*` env vars — with **later sources overriding earlier ones**, so env vars win and `[tool.dotenv]` beats the deprecated `[tool.poetry.plugins.dotenv]`. Values arrive as strings (poetry's parser requires it): `ignore` goes through `_STR_BOOLEAN_MAPPING`, `location` is normalized to `list[pathlib.Path]` by `_as_paths` (comma-separated string allowed). The dataclass `_Config` is the single source of truth for option names and defaults.
4. `loader.load` returns early on `ignore`; otherwise resolves paths from `config.location` (absolute kept as-is, relative joined to `working_dir`) or falls back to `dotenv.core.find(usecwd=True)`, which walks upward from cwd looking for `.env`. Each existing file is applied via `dotenv.core.load` (override + interpolation on).
5. `commands.ActivateCommand` picks an activation script (fish -> `bin/activate.fish`, POSIX -> `bin/activate`, Windows -> `Scripts/Activate.ps1` or `activate.bat`), loads dotenv, then `os.execvp`s the shell — it never returns in practice.

Vendored dotenv package split: `dotenv/parsers.py` (regex/`Reader` character-level parsing of `.env` syntax — quotes, escapes, comments, `export`), `dotenv/variables.py` (POSIX expansion `${VAR}` / `${VAR:-default}`), `dotenv/core.py` (`DotEnv` model, `find`, `load`, `values`, `resolve`).

`logging.Logger` writes at `Verbosity.VERBOSE` only — plugin output is invisible without `-v`, because the plugin runs before the actual command.

## Testing conventions

- `pyproject.toml` `addopts` pins `--basetemp=tests/fixtures` (gitignored) and always runs coverage over `src` with `term-missing`.
- `conftest.create_dotenv_file` writes to `tmp_path / ".." / ".." / ".."`, which resolves to the **repository root** — tests deliberately create real `.env` / `.env.dev` files there so `find(usecwd=True)` picks them up, and `remove_dotenv_file` deletes them. A failing test can leave a stray dotenv file in the repo root.
- Plugin tests mutate the real `os.environ`. Config-source tests isolate with `mock.patch.dict(os.environ, {}, clear=True)` and patch `tomlkit.load` instead of writing a `pyproject.toml`.
- Poetry/cleo interaction is faked with `mocker.MagicMock()` for the event plus a real `EnvCommand()` as `event.command`.

## Code style

- Ruff: `select = ["ALL"]`, line length 100, `fix`/`unsafe-fixes` on, double quotes. Imports single-line, length-sorted, 2 blank lines after; `from __future__ import annotations` is **required in every module** (`required-imports`).
- Per-file ignores in `pyproject.toml` are narrow (tests waive only `INP001`/`S101`); prefer an inline `# noqa` over widening them.
- Docstring openers follow a pattern: modules `"""Module that contains ..."""`, packages `"""Package that contains ..."""`, test modules `"""Module that contains tests for the module that contains ..."""`.
- Comments never end with a period; docstrings keep normal punctuation.
- `ty` (Astral's type checker) targets `python-version = "3.10"` with `unresolved-attribute` / `invalid-argument-type` ignored — preexisting poetry/cleo interop noise, suppressed to keep the gate green.
- `pyupgrade --py310-plus` runs despite the 3.9 floor; the mandatory `from __future__ import annotations` makes the upgraded annotation syntax safe.

## Releases and commits

- Conventional commits (`<type>(<scope>): <subject>`, imperative, lowercase, <=72 chars); branches `<type>/<kebab-description>`. Full type table in `CONTRIBUTING.md`; `cliff.toml` groups `feat`/`fix`/`perf`/`refactor`/... into the changelog.
- Release is manual `workflow_dispatch` on `.github/workflows/release.yaml`: `git-cliff --bumped-version` derives the version from commits (or takes the input override), the workflow runs `poetry version`, regenerates `CHANGELOG.md`, commits + tags `v<version>`, creates the GitHub release, and publishes to PyPI via trusted publishing. **Do not hand-edit `version` in `pyproject.toml` or `CHANGELOG.md` — the workflow owns both.**
- The plugin's config schema is published to the JSON Schema Store; renaming or adding config options means that external schema needs updating too.
- `docs/examples/demo.tape` is a VHS tape that generates `docs/assets/demo.gif`; `docs/examples/configs/` holds the sample `pyproject.toml` variants used in the demo.
