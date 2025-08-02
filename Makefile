help:
		@echo Usage:
		@echo make install-backend-dev
		@echo make run-backend-dev

install-backend-dev:
		python3 -m venv venv --prompt FireRSS
		venv/bin/pip install -U pip
		venv/bin/pip install -e 'backend[dev]'
		venv/bin/pre-commit install --install-hooks

run-backend-dev:
		venv/bin/python -m fastapi dev backend/fire_rss/main.py
