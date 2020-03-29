import os

from xeddsa import XEdDSA25519

def test_signing():
    for _ in range(100):
        msg = os.urandom(100)

        for _ in range(100):
            mont_priv = XEdDSA25519.generate_mont_priv()
            mont_pub  = XEdDSA25519.mont_pub_from_mont_priv(mont_priv)

            signing_xeddsa   = XEdDSA25519(mont_priv = mont_priv)
            verifying_xeddsa = XEdDSA25519(mont_pub  = mont_pub)

            assert verifying_xeddsa.verify(msg, signing_xeddsa.sign(msg))
