.PHONY: clean coverage lint requirements test_integration test_unit

PYTEST ?= pytest
FLAKE8 ?= flake8

clean:
	@find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -delete

coverage:
	@$(PYTEST) --cov=domain --cov=infrastructure test

lint:
	@$(FLAKE8) domain infrastructure test

requirements:
	@pip install -r requirements.txt

test_integration:
	@$(PYTEST) -m 'integration' test

test_unit:
	@$(PYTEST) -m 'not integration' test
