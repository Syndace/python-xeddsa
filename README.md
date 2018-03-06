# python-xeddsa
#### A python implementation of the XEdDSA signature scheme.

This python library offers an open implementation of the XEdDSA signature scheme as specified [here](https://signal.org/docs/specifications/xeddsa/).

## !!! IMPORTANT WARNING !!!
This code was not written by a cryptographer and is most probably *NOT SECURE*.
It is most probably *NOT RESISTENT TO SIDE CHANNEL ATTACKS* and you should *NOT USE IT IN PRODUCTION* if you don't REALLY know what you're doing.

The next goal is a rewrite of the cryptography to use a (what people consider) safe implementation like ref10 instead of self-written code.
