.PHONY: all test clean requirements

PYTEST ?= pytest
FLAKE8 ?= flake8

clean:
	@find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -delete

coverage:
	@$(PYTEST) -v --cov=domain test

lint:
	@$(FLAKE8) domain test

requirements:
	@pip install -r requirements.txt

test:
	@$(PYTEST) -v test
