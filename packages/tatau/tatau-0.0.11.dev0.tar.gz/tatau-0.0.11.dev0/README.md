# Tatau

![Build Status](https://drone.tatau.io/api/badges/TatauCloud/tatau/status.svg?branch=develop)


Tatau is a distributed supercomputing platform used by AI
companies to perform complex deep-learning operations
more cost-effectively, and efficiently than other alternatives.

You can find full API documentation on [ReadTheDocs](https://tatau.readthedocs.io/en/develop/)
 
## How to contribute

Install dev requirements

```bash
pip install -r requirements.dev.txt
```

Run tests

```bash
tox
```

Build docs

```bash
tox -e docs
```

Run lint
```bash
tox -e lint
```
