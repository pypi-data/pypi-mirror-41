python-fastpurge
================

A Python client for the [Akamai Fast Purge API](https://developer.akamai.com/api/core_features/fast_purge/v3.html).

[![Build Status](https://travis-ci.org/release-engineering/python-fastpurge.svg?branch=master)](https://travis-ci.org/release-engineering/python-fastpurge)
[![Coverage Status](https://coveralls.io/repos/github/release-engineering/python-fastpurge/badge.svg?branch=master)](https://coveralls.io/github/release-engineering/python-fastpurge?branch=master)

- [Source](https://github.com/release-engineering/python-fastpurge)
- [Documentation](https://release-engineering.github.io/python-fastpurge/)
- [PyPI](https://pypi.org/project/fastpurge)

This library provides a simple asynchronous Python wrapper for the Fast Purge
API. Features include:

- convenient handling of authentication
- recovery from errors
- splitting large requests into smaller pieces


Example
-------

Assuming a valid `~/.edgerc` file prepared with credentials according to
Akamai's documentation:

```python
from fastpurge import FastPurgeClient

# Omit credentials to read from ~/.edgerc
client = FastPurgeClient()

# Start purge of some URLs
purged = client.purge_by_url(['https://example.com/resource1', 'https://example.com/resource2'])

# purged is a Future, if we want to ensure purge completed
# we can block on the result:
result = purged.result()
print("Purge completed:", result)
```


License
-------

GPLv3
