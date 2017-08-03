.PHONY: clean coverage lint requirements test_integration test_unit

PYTEST ?= pytest
FLAKE8 ?= flake8
FLASK ?= flask

clean:
	@find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -delete

coverage:
	@$(PYTEST) -m 'not integration' --cov=domain test

lint:
	@$(FLAKE8) domain infrastructure test

requirements:
	@pip install -r requirements.txt

run:
	@PYTHONPATH="$(PYTHONPATH):./infrastructure" FLASK_APP=infrastructure/application/app.py \
	$(FLASK) run

test_integration:
	@$(PYTEST) -m 'integration' test

test_unit:
	@$(PYTEST) -m 'not integration' test
