.PHONY: all test clean requirements

clean:
	@find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -delete

lint:
	@flake8 domain test

requirements:
	@pip install -r requirements.txt

test:
	@python -m unittest discover --start-directory test
