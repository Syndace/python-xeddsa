import os

from xeddsa.implementations import XEdDSA25519

def test_signing():
    for _ in range(50):
        message = os.urandom(50)

        for _ in range(50):
            mont_priv = XEdDSA25519.generateDecryptionKey()
            mont_pub  = XEdDSA25519.restoreEncryptionKey(mont_priv)

            signing_xeddsa   = XEdDSA25519(decryption_key = mont_priv)
            verifying_xeddsa = XEdDSA25519(encryption_key = mont_pub)

            assert verifying_xeddsa.verify(message, signing_xeddsa.sign(message))
