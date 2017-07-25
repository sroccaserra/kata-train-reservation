## Original Kata

The original kata by [@emilybache](https://twitter.com/emilybache) is here, complete with doc & starting code in various languages:

- <https://github.com/emilybache/KataTrainReservation>


## See Also

Live implementation of the kata at "L’après-midi du DDD - live coding" (french):

- <https://www.youtube.com/playlist?list=PLGl1Jc8ErU1xmSImIQ27Biu46C4MQHTfK>

## Status

**WIP**

Next steps:

- [ ] Design: move serialization-like structure out to train data service adapter
- [ ] Implement: multi coach trains
- [ ] Implement: external service providers
- [ ] Implement: application server
- [ ] ...

## Tech details

Tested with [Python 3.6.2](https://www.python.org/downloads/release/python-362/).

See `Makefile` for more tech details.

### Pre-commit hook

Example of pre-commit hook (`.git/hooks/pre-commit`):

```sh
#!/bin/sh

export PYTEST=~/.pyenv/versions/3.6.2/bin/pytest
export FLAKE8=~/.pyenv/versions/3.6.2/bin/flake8

make lint
make test_unit
```