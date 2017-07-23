.PHONY: all test clean

test:
	@python -m unittest discover --start-directory test

clean:
	@find . \( -name \*.pyc -o -name \*.pyo -o -name __pycache__ \) -prune -delete
