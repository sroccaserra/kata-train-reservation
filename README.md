## Original Kata

The original kata by [@emilybache](https://twitter.com/emilybache) is here, complete with doc & starting code in various languages:

- <https://github.com/emilybache/KataTrainReservation>


## See Also

Live implementation of the kata at "L’après-midi du DDD - live coding" (french):

- <https://www.youtube.com/playlist?list=PLGl1Jc8ErU1xmSImIQ27Biu46C4MQHTfK>

## Tech details

Tested with [Python 3.4.5](https://www.python.org/download/releases/3.4.5/).

See `Makefile` for more tech details.

### Pre-commit hook

Example of pre-commit hook (`.git/hooks/pre-commit`):

```sh
#!/bin/sh

export PYTEST=~/.pyenv/versions/3.4.5/bin/pytest
export FLAKE8=~/.pyenv/versions/3.4.5/bin/flake8

make lint
make test
```