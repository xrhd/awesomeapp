.PHONY: run test install lint

VENV = .venv/bin
PYTHON = $(VENV)/python
PYTEST = $(VENV)/pytest
FASTAPI = $(VENV)/fastapi

# Run the development server
run:
	$(FASTAPI) dev src/main.py

# Run integration tests
test:
	PYTHONPATH=. $(PYTEST)

# Install dependencies
install:
	uv sync
