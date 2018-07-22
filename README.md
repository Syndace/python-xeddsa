[![Build Status](https://travis-ci.org/Syndace/python-xeddsa.svg?branch=master)](https://travis-ci.org/Syndace/python-xeddsa)

# python-xeddsa
#### A python implementation of the XEdDSA signature scheme.

This python library offers an open implementation of the XEdDSA signature scheme as specified [here](https://signal.org/docs/specifications/xeddsa/).

### !!! IMPORTANT WARNING !!!
This code was not written by a cryptographer and is most probably **NOT SECURE**.

#### Ref10
The python-xeddsa library uses the ref10 C & ASM implementation of curve25519 and ed25519 found in the ref10 directory.

To build the required files, just run `make` in the `ref10/` directory.

This step creates the shared object files `libcrypto_scalarmult.so` and `libcrypto_sign.so` as well as preprocessed headers required to build the Python [cffi](https://bitbucket.org/cffi/cffi) modules.

Make sure the shared object files can be found by Python, e.g. by adding `ref10/bin/` to the `LD_LIBRARY_PATH` environment variable.

Now you can run `python setup.py install` to install the package as usual.

### NOTICE
This implementation is meant as a transitional solution until one of the big crypto-libraries like libsodium picks up XEdDSA.
The [version 1.0 roadmap](https://download.libsodium.org/doc/internals/roadmap.html) of libsodium lists XEdDSA, it might only take a few more months to get a stable and secure implementation.
