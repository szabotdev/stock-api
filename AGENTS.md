# Repository Guidelines

## Project Structure & Module Organization
This repository is a small Flask API and UI app.
- `app/` contains the package code:
  - `app/routes/` holds Flask blueprints (`ui.py`, `tickers.py`, `prices.py`).
  - `app/storage.py` handles reading and writing ticker data.
  - `app/config.py` defines runtime configuration, including `TICKERS_FILE`.
- `app/templates/` contains Jinja templates such as `index.html`.
- `data/` stores runtime JSON data, especially `tickers.json`.
- `run.py` is the Flask entrypoint used by Docker and local runs.

## Build, Test, and Development Commands
The project does not currently include a dedicated test or lint configuration.
- `python run.py` starts the app on `http://0.0.0.0:5001`.
- `docker compose up --build` builds the image and runs the service with `./data` mounted to `/data`.
- `pip install -r requirements.txt` installs the Python dependencies (`flask`, `yfinance`).
- `make test` runs the pytest suite through `.venv/bin/python -m pytest`.

## Coding Style & Naming Conventions
Use Python 3.12 compatible code, 4-space indentation, and standard Flask patterns.
- Prefer `snake_case` for functions, variables, and module names.
- Use `Blueprint` modules under `app/routes/` for HTTP endpoints.
- Keep file and symbol names aligned with the existing structure, for example `prices_bp`, `load_tickers()`, and `tickers.json`.
- No formatter is enforced in-repo, so keep changes consistent with surrounding code.

## Testing Guidelines
There is no committed automated test suite yet. If you add tests, use `pytest` and place them under `tests/` with names like `test_prices.py`.
- Focus coverage on route behavior, ticker persistence, and error handling around `yfinance` calls.
- Prefer deterministic tests by mocking network access instead of hitting live market data.

## Commit & Pull Request Guidelines
Current history is short and uses concise imperative subjects, such as `Fix dockerfile` and `Add Docker build workflow`.
- Keep commit messages short and action-focused.
- Pull requests should describe the behavior change, note any configuration or data-file impact, and include screenshots for UI changes when relevant.
- Mention any manual verification steps, especially when routes or Docker behavior changes.

## Configuration Notes
`TICKERS_FILE` defaults to `/data/tickers.json`. When running locally without Docker, set it explicitly if you want to avoid writing outside the repository.
