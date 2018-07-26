[![Build Status](https://travis-ci.org/Syndace/python-xeddsa.svg?branch=master)](https://travis-ci.org/Syndace/python-xeddsa)

# python-xeddsa
#### A python implementation of the XEdDSA signature scheme.

This python library offers an open implementation of the XEdDSA signature scheme as specified [here](https://signal.org/docs/specifications/xeddsa/).

### !!! IMPORTANT WARNING !!!
This code was not written by a cryptographer and is most probably **NOT SECURE**.

### Installation

The python-xeddsa library uses the ref10 C & ASM implementation of curve25519 and ed25519 found in the ref10 directory.

#### Building ref10 on Linux
On Linux, building the required libraries is as simple as running `make` in the `ref10/` directory.

#### Building ref10 on Windows
On Windows, building the required libraries is about as easy as on Linux, but you need to install some software first:
- [MinGW](http://www.mingw.org/) or [MinGW-w64](https://mingw-w64.org/doku.php)
- The Microsoft Visual C++ Build Tools. Those can be installed using the standalone version you can download [here](https://visualstudio.microsoft.com/downloads/), or as part of Visual Studio, for example the free [Community Edition](https://visualstudio.microsoft.com/vs/community/).

Now, open your MinGW terminal and run `make` or `mingw32-make` (whatever works) in the `ref10/` directory.

#### Finalizing the installation
After building ref10, you can use `python setup.py install` to install python-xeddsa as you're used to.

### NOTICE
This implementation is meant as a transitional solution until one of the big crypto-libraries like libsodium picks up XEdDSA.
The [version 1.0 roadmap](https://download.libsodium.org/doc/internals/roadmap.html) of libsodium lists XEdDSA, it might only take a few more months to get a stable and secure implementation.
