# Python Package Skeleton

Example of how to configure and test a python package.

## Prerequisites

* python
* virtualenv

## Installation

This package is intended for local testing in a virtual environment.
It has not been published to PyPi so it must be installed from a cloned copy of the git repo.
```
$ git clone git@github.com:KevinWMatthews/python-package_skeleton.git
$ cd python-package_skeleton
```

Create and activate a virtual environment:
```
$ virtualenv -p python3 venv
$ source venv/bin/activate
```

Install into your virtual environment:
```
$ pip install .
```

Of course, don't forget to deactivate the virtual environment using `deactivate`.

### Usage

Example scripts will be installed in the virtual environment (located in `venv/bin/`).
Run them with, for example,
```
$ skeleton_rattle
Rattle rattle!
```

### Development

Clone the repo and create a virtual environment as above but instead of installing
the package itself, install the package requirements:
```
$ pip install -r requirements.txt
```

Run tests:
```
$ python -m pytest
```

If you wish to install the package into your virtual environment,
install in "editable" (develop) mode:
```
pip install -e .
```
If this is done, run the tests using simply:
```
pytest
```
