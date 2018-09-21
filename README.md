[![PyPI](https://img.shields.io/pypi/v/XEdDSA.svg)](https://pypi.org/project/XEdDSA/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/XEdDSA.svg)](https://pypi.org/project/XEdDSA/)
[![Build Status](https://travis-ci.org/Syndace/python-xeddsa.svg?branch=master)](https://travis-ci.org/Syndace/python-xeddsa)

# python-xeddsa
#### A python implementation of the XEdDSA signature scheme.
This python library offers an open implementation of the XEdDSA signature scheme as specified [here](https://signal.org/docs/specifications/xeddsa/).

### !!! IMPORTANT WARNING !!!
This code was not written by a cryptographer and is most probably **NOT SECURE**.

### Installation
Install the package using pip (`pip install XEdDSA`) or manually using `python setup.py install`, as you're used to.

__NOTE__: On UNIX, the installation uses the `cmake`, `make` and `gcc` tools.

__NOTE__: On Windows, precompiled binaries are downloaded during the installation.
Make sure you have an active internet connection and access to `https://github.com`.
The installation requires the Microsoft Visual C++ Build Tools.
Those can be installed using the standalone version you can download [here](https://visualstudio.microsoft.com/downloads/),
or as part of Visual Studio, for example the free [Community Edition](https://visualstudio.microsoft.com/vs/community/). 

### Manually building ref10
Following section explains how to manually compile the ref10 library, which is __not__ required when using pip or `python setup.py install`.

For detailed information on what the ref10 library is and how it was built, look at `ref10/README.md`.

#### Building ref10 on UNIX
On UNIX, run following commands to build the ref10 library:

```Bash
$ cd ref10/
$ mkdir build
$ cd build/
$ cmake ..
$ make
```

To clean up the build artifacts, just delete the whole build and bin directories inside of the ref10 directory.

#### Building ref10 on Windows
__TODO__

### NOTICE
This implementation is meant as a transitional solution until one of the big crypto-libraries like libsodium picks up XEdDSA.
The [version 1.0 roadmap](https://download.libsodium.org/doc/internals/roadmap.html) of libsodium lists XEdDSA, it might only take a few more months to get a stable and secure implementation.
