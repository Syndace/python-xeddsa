import os

from xeddsa.implementations import XEdDSA25519

from test_conversion import montgomery_private_keys

def test_signing():
    for _ in range(100):
        message = os.urandom(100)

        for mont_priv in montgomery_private_keys:
            xeddsa = XEdDSA25519(decryption_key = mont_priv)

            assert xeddsa.verify(message, xeddsa.sign(message))
