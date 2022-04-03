[![PyPI](https://img.shields.io/pypi/v/XEdDSA.svg)](https://pypi.org/project/XEdDSA/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/XEdDSA.svg)](https://pypi.org/project/XEdDSA/)
[![Build Status](https://travis-ci.org/Syndace/python-xeddsa.svg?branch=stable)](https://travis-ci.org/Syndace/python-xeddsa)
[![Documentation Status](https://readthedocs.org/projects/python-xeddsa/badge/?version=latest)](https://python-xeddsa.readthedocs.io/en/latest/?badge=latest)

# python-xeddsa #

Python bindings to [libxeddsa](https://github.com/Syndace/libxeddsa).

## Installation ##

python-xeddsa depends on two system libraries, [libxeddsa](https://github.com/Syndace/libxeddsa)>=2,<3 and [libsodium](https://download.libsodium.org/doc/).

Install the latest release using pip (`pip install XEdDSA`) or manually from source by running `pip install .` (preferred) or `python setup.py install` in the cloned repository. The installation requires libsodium and the Python development headers to be installed. If a locally installed version of libxeddsa is available, python-xeddsa tries to use that. Otherwise it uses prebuilt binaries of the library, which are available for Linux, MacOS and Windows on the amd64 architecture. Set the `LIBXEDDSA_FORCE_LOCAL` environment variable to forbid the usage of prebuilt binaries.

## Testing, Type Checks and Linting ##

python-omemo uses [pytest](https://docs.pytest.org/en/latest/) as its testing framework, [mypy](http://mypy-lang.org/) for static type checks and both [pylint](https://pylint.pycqa.org/en/latest/) and [Flake8](https://flake8.pycqa.org/en/latest/) for linting. All tests/checks can be run locally with the following commands:

```sh
$ pip install pytest pytest-asyncio mypy pylint flake8
$ export MYPYPATH=stubs/
$ mypy --strict xeddsa/ setup.py libxeddsa/ tests/
$ pylint xeddsa/ setup.py libxeddsa/ tests/
$ flake8 xeddsa/ setup.py libxeddsa/ tests/
$ pytest
```

## Documentation ##

View the documentation on [readthedocs.io](https://python-xeddsa.readthedocs.io/) or build it locally, which requires the Python packages listed in `docs/requirements.txt`. With all dependencies installed, run `make html` in the `docs/` directory. You can find the generated documentation in `docs/_build/html/`.

## Travis CI ##

The project used to be built using Travis CI, which was amazing. Sadly, Travis fully closed their open-source support. I have yet to migrate somewhere else, until then the project will not be automatically tested.
