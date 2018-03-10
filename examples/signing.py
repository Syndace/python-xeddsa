from __future__ import print_function

import os

from xeddsa.implementations import XEdDSA25519

from conversion import montgomery_private_keys

if __name__ == "__main__":
    message = os.urandom(100)
    nonce   = os.urandom(64)

    tests = 0
    successes = 0

    for mont_priv in montgomery_private_keys:
        xeddsa = XEdDSA25519(decryption_key = mont_priv)

        signature = xeddsa.sign(message, nonce)

        if xeddsa.verify(message, signature):
            print("Test #" + str(tests + 1) + " successful!")
            successes += 1
        else:
            print("")
            print("Test #" + str(tests + 1) + " failed.")

        tests += 1

    print("All tests done, " + str(successes) + "/" + str(tests) + " successful.")
