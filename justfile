format:
  find src -type f -name '*.py' | xargs poetry run pyupgrade --py39-plus
  find tests -type f -name '*.py' | xargs poetry run pyupgrade --py39-plus
  poetry run ruff format .

lint:
  poetry run ty check .
  poetry run ruff check .

test:
  poetry run pytest .

update:
  poetry update
