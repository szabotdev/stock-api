.PHONY: install run test

install:
	uv pip install --python .venv/bin/python -r requirements.txt

run:
	.venv/bin/python run.py

test:
	.venv/bin/python -m pytest
