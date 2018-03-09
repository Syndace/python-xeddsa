# python-xeddsa
#### A python implementation of the XEdDSA signature scheme.

This python library offers an open implementation of the XEdDSA signature scheme as specified [here](https://signal.org/docs/specifications/xeddsa/).

### !!! IMPORTANT WARNING !!!
This code was not written by a cryptographer and is most probably **NOT SECURE**.
It is most probably **NOT RESISTENT TO SIDE CHANNEL ATTACKS** and you should **NOT USE IT IN PRODUCTION** if you don't REALLY know what you're doing.

I hope some cryptographer can confirm/improve the security of this code in the near future.

#### Ref10
The python-xeddsa library uses the ref10 Ed25519 C & ASM implementation found in the ref10 directory.
Building ref10 requires libsodium to be installed.
The library headers of libsodium are expected to be located in `/usr/local/include/sodium/` - if that's not the case, please correct the Makefile located in ref10 accordingly.

Your `LD_LIBRARY_PATH` environment variable is expected to point to the path the `libsodium.so` and `libsodium.a` files can be found.

If these requirements are met, the ref10 library can be built by running `make` in the ref10 directory.

Now, add the newly created directory path `ref10/bin` to your `PATH` and your `LD_LIBRARY_PATH` environment variables or move the `libref10.so` manually and you're set!

The ref10 implementation is released under creative commons license.

### NOTICE
This implementation is meant as a transitional solution until one of the big crypto libraries like libsodium picks up XEdDSA.
Please expect this implementation to disappear at some point.
