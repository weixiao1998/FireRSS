help:
		@echo Usage:
		@echo make install-dev
		@echo make run-backend

install-dev:
		python3 -m venv .venv --prompt FireRSS
		.venv/bin/pip install -U pip
		.venv/bin/pip install -e backend[dev]
		.venv/bin/pip install -r backend/requirements.txt
		.venv/bin/pre-commit install --install-hooks

run-backend:
		.venv/bin/python -m backend.fire_rss.app
