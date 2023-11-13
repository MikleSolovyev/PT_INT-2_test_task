.DEFAULT_GOAL: run

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip
PYTEST = $(VENV)/bin/pytest

run: $(VENV)/bin/activate
	$(PYTHON) src/main.py

test: $(VENV)/bin/activate
	$(PYTEST) tests

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	find -name .pytest_cache -exec rm -rf {} +
	find -name '*.pyc' -delete
	find -name __pycache__ -exec rm -rf {} +
	rm -rf $(VENV)