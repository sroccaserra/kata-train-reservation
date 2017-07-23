.PHONY: all test clean requirements

PYTHON ?= python

clean:
	@find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -delete

lint:
	@flake8 domain test

requirements:
	@pip install -r requirements.txt

test:
	@$(PYTHON) -m unittest discover --start-directory test
