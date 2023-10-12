# Variables
VENV_NAME?=venv
VENV_ACTIVATE=. $(VENV_NAME)/bin/activate

# ---

# The default target, when you run 'make' with no arguments
all: venv


# Create a virtual environment
venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate:
	python3 -m venv $(VENV_NAME)
	${VENV_ACTIVATE} && pip install -r requirements.txt
	${VENV_ACTIVATE} && pip install -r requirements-dev.txt

# ---

# Install the library into the virtual environment
install: venv
	${VENV_ACTIVATE} && pip install .

# Build the library distribution package
build: venv
	${VENV_ACTIVATE} && python setup.py sdist bdist_wheel

# Install the library for tests
install-dev: venv
	${VENV_ACTIVATE} && pip install -e .

# Run tests (intended to be run after the library has been installed for tests)
test: venv
	${VENV_ACTIVATE} && pytest -v

# ---

# Clean build artifacts
clean-dist:
	rm -rf build dist src/*.egg-info

# Clean Python cache files
clean-cache:
	find . -type f -name '*.pyc' -delete
	find . -type d -name '__pycache__' -delete
	rm -rf .pytest_cache/

# Remove virtual environment (together with possible development install)
clean-venv:
	rm -rf $(VENV_NAME)

# Full cleanup
clean-all: clean-dist clean-cache clean-venv

# ---

# Useful aliases
.PHONY: all venv install build install-dev test clean-dist clean-cache clean-venv clean-all
