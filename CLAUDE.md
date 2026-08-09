# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Poetry **application plugin** (entry point `poetry.application.plugin` → `poetry_plugin_dotenv.plugin:DotenvPlugin`) that loads a dotenv file into `os.environ` before any `poetry` command runs, and adds a `poetry activate` command that re-execs the user's shell with the venv activated.

Hard constraints that shape the code:

- Must work on both `poetry >=1.5,<3` and Python `>=3.9,<4`.
- **No runtime dependencies beyond `poetry` itself.** `src/poetry_plugin_dotenv/dotenv/` is a vendored fork of `python-dotenv` specifically to keep it that way — do not add `python-dotenv` or any other runtime dep.

## Commands

`just` is the entry point for every task (`justfile`); CI runs the same recipes.

- `just install` — `poetry install --all-groups --all-extras`
- `just format` — `uvx pyupgrade --py310-plus` over all `.py`, then `uvx ruff check --fix .`, then `uvx ruff format .`
- `just lint` — `uvx ruff check .` then `uvx ty check`
- `just test` — `poetry run pytest`; silently skipped when a `.no-tests` sentinel file exists
- `just check` — `lint` + `test`
- `just audit` — `uvx pip-audit`
- `just update` — `poetry update`

Formatters and linters run through `uvx` (uv-managed, outside the project venv); only tests run through `poetry run`.

Single test: `poetry run pytest tests/test_plugin.py::test_default_dotenv_file` or `poetry run pytest -k <pattern>`.

## Architecture

Per-command flow:

1. `plugin.DotenvPlugin.activate` registers `load` as a listener on cleo's `COMMAND` event and registers the `activate` command factory.
2. `plugin.load` resolves `working_dir` from the `--directory` option (else cwd), builds `logging.Logger(event)` and `configurator.Config(working_dir)`, and calls `loader.load`. Commands in `plugin.COMMANDS_EXCLUSION` (`{"activate"}`) are skipped — `ActivateCommand` does its own loading.
3. `configurator.Config` iterates `CONFIG_SOURCES` in order — `[tool.poetry.plugins.dotenv]`, then `[tool.dotenv]` (both in `pyproject.toml`), then `POETRY_PLUGIN_DOTENV_*` env vars — with **later sources overriding earlier ones**, so env vars win. Values arrive as strings (poetry's parser requires it): `ignore` goes through `_STR_BOOLEAN_MAPPING`, `location` is normalized to `list[pathlib.Path]` by `_as_paths` (comma-separated allowed). The dataclass `_Config` is the single source of truth for option names and defaults.
4. `loader.load` returns early on `ignore`; otherwise resolves paths from `config.location` (absolute kept as-is, relative joined to `working_dir`) or falls back to `dotenv.core.find(usecwd=True)`, which walks upward from cwd looking for `.env`. Each existing file is applied via `dotenv.core.load`.
5. `commands.ActivateCommand` picks an activation script (fish → `activate.fish`, POSIX → `activate`, Windows → `Scripts/Activate.ps1` or `activate.bat`), loads dotenv, then `os.execvp`s the shell. It never returns in practice.

Vendored dotenv package split: `parsers.py` (character-level `Reader` over `.env` syntax — quotes, escapes, comments, `export`), `variables.py` (POSIX expansion `${VAR}` / `${VAR:-default}`), `core.py` (`DotEnv` model, `find`, `load`, `values`).

`logging.Logger` writes at `Verbosity.VERBOSE` only — plugin output is invisible without `-v`, because the plugin runs before the actual command.

## Testing conventions

- `pyproject.toml` `addopts` pins `--basetemp=tests/fixtures` (gitignored) and always runs coverage over `src`.
- `conftest.create_dotenv_file` writes to `tmp_path / ".." / ".." / ".."`, which resolves to the **repository root** — tests deliberately create real `.env` / `.env.dev` files there so `find(usecwd=True)` picks them up, then `remove_dotenv_file` deletes them. A failing test can leave a stray dotenv file in the repo root.
- Plugin tests mutate the real `os.environ`. Config-source tests isolate with `@mock.patch.dict(os.environ, {}, clear=True)` and patch `tomlkit.load` rather than writing a `pyproject.toml`.
- Poetry/cleo interaction is faked with `mocker.MagicMock()` for the event plus a real `EnvCommand()` as `event.command`.

## Code style

- Ruff: `select = ["ALL"]`, line length 100, `fix`/`unsafe-fixes` on, double quotes. Imports are single-line, sorted by length, 2 blank lines after. `from __future__ import annotations` is **required in every module** (`required-imports`).
- Per-file ignores are narrow — tests only waive `INP001` and `S101`. Prefer an inline `# noqa` with a reason over widening the ignore lists.
- Module docstrings open with `Module that contains ...`; `__init__.py` with `Package that contains ...`; test modules with `Module that contains tests for ...` (nesting the description of the module under test).
- Comments never end with a period; docstrings do.
- `ty` (Astral's type checker) targets `python-version = "3.10"` and has `unresolved-attribute` / `invalid-argument-type` suppressed in `pyproject.toml` — preexisting issues in the poetry/cleo interop layer, suppressed to keep the gate green.
- `pyupgrade --py310-plus` runs despite the 3.9 floor; the `from __future__ import annotations` requirement covers the resulting annotation syntax.

## Releases

- Conventional commits (`<type>(<scope>): <subject>`), branches `<type>/<kebab-description>` — see `CONTRIBUTING.md` for the full type table.
- Release is manual `workflow_dispatch` on `.github/workflows/release.yaml`: `git-cliff --bumped-version` picks the version, CI runs `poetry version`, regenerates `CHANGELOG.md` via `cliff.toml`, tags, releases, and publishes to PyPI. **Do not hand-edit `version` in `pyproject.toml` or `CHANGELOG.md`.**
- The plugin's config schema is published to [JSON Schema Store](https://www.schemastore.org/json); renaming or adding options means the external schema needs updating too.
