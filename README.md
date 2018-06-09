# python-xeddsa
#### A python implementation of the XEdDSA signature scheme.

This python library offers an open implementation of the XEdDSA signature scheme as specified [here](https://signal.org/docs/specifications/xeddsa/).

### !!! IMPORTANT WARNING !!!
This code was not written by a cryptographer and is most probably **NOT SECURE**.
It is most probably **NOT RESISTENT TO SIDE CHANNEL ATTACKS** and you should **NOT USE IT IN PRODUCTION** if you don't REALLY know what you're doing.

I hope some cryptographer can confirm/improve the security of this code in the near future.

#### Ref10
The python-xeddsa library uses the ref10 C & ASM implementation of curve25519 and ed25519 found in the ref10 directory.

Just run `make` in the `ref10` directory and it should generate the two required files: `ref10/bin/crypto_scalarmult.so` and `ref10/bin/crypto_sign.so`.
Please make sure these files can be found using your PATH environment variable.

### NOTICE
This implementation is meant as a transitional solution until one of the big crypto-libraries like libsodium picks up XEdDSA.
The [version 1.0 roadmap](https://download.libsodium.org/doc/internals/roadmap.html) of libsodium lists XEdDSA, it might only take a few more months to get a stable and secure implementation.
