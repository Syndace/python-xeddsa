[![PyPI](https://img.shields.io/pypi/v/XEdDSA.svg)](https://pypi.org/project/XEdDSA/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/XEdDSA.svg)](https://pypi.org/project/XEdDSA/)
[![Build Status](https://github.com/Syndace/python-xeddsa/actions/workflows/test-and-publish.yml/badge.svg)](https://github.com/Syndace/python-xeddsa/actions/workflows/test-and-publish.yml)
[![Documentation Status](https://readthedocs.org/projects/python-xeddsa/badge/?version=latest)](https://python-xeddsa.readthedocs.io/)

**_This repository is actively maintained._**

Activity is low at times because this project is already feature-complete, documented and tested.

# python-xeddsa #

Python bindings to [libxeddsa](https://github.com/Syndace/libxeddsa).

## Installation ##

python-xeddsa depends on two system libraries, [libxeddsa](https://github.com/Syndace/libxeddsa)>=2,<3 and [libsodium](https://download.libsodium.org/doc/).

Install the latest release using pip (`pip install XEdDSA`), from the wheels available in the artifacts of the [Test & Publish workflow](https://github.com/Syndace/python-xeddsa/actions/workflows/test-and-publish.yml), or manually from source by running `pip install .` in the cloned repository. The installation from source requires libxeddsa, libsodium and the Python development headers to be installed.

## Testing, Type Checks and Linting ##

python-xeddsa uses [pytest](https://docs.pytest.org/en/latest/) as its testing framework, [mypy](http://mypy-lang.org/) for static type checks and both [pylint](https://pylint.pycqa.org/en/latest/) and [Flake8](https://flake8.pycqa.org/en/latest/) for linting. All tests/checks can be run locally with the following commands:

```sh
$ pip install --upgrade .[test,lint]
$ mypy xeddsa/ setup.py libxeddsa/ tests/
$ pylint xeddsa/ setup.py libxeddsa/ tests/
$ flake8 xeddsa/ setup.py libxeddsa/ tests/
$ pytest
```

## Usage with Brython ##

python-xeddsa can be used in the browser with Brython, thanks to the Emscripten build of libxeddsa. Refer to `tests/test_brython.html` for the setup routine required to load the Emscripten build for usage with Brython. In summary, Brython's initialization is deferred until after the libxeddsa WebAssembly module and wrapper have been loaded. Other than that, python-xeddsa can be used as usual and handled with Brython like a pure Python package.

The tests can be run with Brython by running the following commands from the root of this repository:

```
$ # You need brython-cli in the version fitting your local Python installation
$ pip install brython==$YOUR_PYTHON_VERSION
$ cd xeddsa/
$ # Older versions of brython-cli use `--make_package` instead of just `make_package`
$ brython-cli --make_package xeddsa
$ cd ../
$ python3 -m http.server 8080
$ xdg-open http://localhost:8080/tests/test_brython.html
```

You'll find the output in the browser's dev console.

## Documentation ##

View the documentation on [readthedocs.io](https://python-xeddsa.readthedocs.io/) or build it locally. Additional requirements to build the docs can be installed using `pip install .[docs]`. With all dependencies installed, run `make html` in the `docs/` directory. You can find the generated documentation in `docs/_build/html/`.
