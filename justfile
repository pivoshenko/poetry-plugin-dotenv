default:
    @just --list

install:
    poetry install --all-groups --all-extras

format:
    find src -type f -name '*.py' | xargs uvx pyupgrade --py310-plus
    find tests -type f -name '*.py' | xargs uvx pyupgrade --py310-plus
    uvx ruff check --fix .
    uvx ruff format .

lint:
    uvx ruff check .
    uvx ruff format --check .
    uvx ty check

test:
    uvx pytest

check: lint test

update:
    poetry update

audit:
    uvx pip-audit
