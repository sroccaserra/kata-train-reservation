
- <https://github.com/emilybache/KataTrainReservation>

Tested with [Python 3.4.5](https://www.python.org/download/releases/3.4.5/)

## Pre-commit hook

Example of pre-commit hook (`.git/hooks/pre-commit`):

```sh
#!/bin/sh

export PYTEST=~/.pyenv/versions/3.4.5/bin/pytest
export FLAKE8=~/.pyenv/versions/3.4.5/bin/flake8

make lint
make test
```