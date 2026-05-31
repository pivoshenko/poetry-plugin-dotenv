default:
    @just --list

install:
    poetry install --all-groups --all-extras

format:
    find src -type f -name '*.py' | xargs poetry run pyupgrade --py310-plus
    find tests -type f -name '*.py' | xargs poetry run pyupgrade --py310-plus
    poetry run ruff format .

lint:
    poetry run ty check .
    poetry run ruff check .

test:
    poetry run pytest .

check: lint test

update:
    poetry update
