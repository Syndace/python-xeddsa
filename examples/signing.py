import os

from xeddsa.implementations import XEdDSA25519

from conversion import montgomery_private_keys, bytesToString, toBytes

if __name__ == "__main__":
    message = toBytes(os.urandom(256))
    nonce   = toBytes(os.urandom(64))

    tests = 0
    successes = 0

    for mont_priv in montgomery_private_keys:
        xeddsa = XEdDSA25519(decryption_key = bytesToString(mont_priv))

        signature = xeddsa.sign(message, nonce)

        if xeddsa.verify(message, signature):
            print "Test #" + str(tests + 1) + " successful!"
            successes += 1
        else:
            print ""
            print "Test #" + str(tests + 1) + " failed."

        tests += 1

    print "All tests done, " + str(successes) + "/" + str(tests) + " successful."
