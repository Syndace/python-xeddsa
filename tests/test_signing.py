import os

from xeddsa.implementations import XEdDSA25519

def test_signing():
    for _ in range(50):
        message = os.urandom(50)

        for _ in range(50):
            mont_priv = XEdDSA25519.generate_mont_priv()
            mont_pub  = XEdDSA25519.mont_pub_from_mont_priv(mont_priv)

            signing_xeddsa   = XEdDSA25519(mont_priv = mont_priv)
            verifying_xeddsa = XEdDSA25519(mont_pub  = mont_pub)

            assert verifying_xeddsa.verify(message, signing_xeddsa.sign(message))

def test_special():
    mont_pub  = (b"\x47\xb5\xa3\xf4\xf0\xc9\x8c\xe6\x2f\xc1\x90\xe0\xec\xdb\x4e\x89" +
                 b"\x48\xb4\xfb\x38\xec\x3b\x82\x75\x64\xa3\x5e\xc8\x8a\xcf\x1a\x55" )

    signature = (b"\x21\x0c\x42\xdd\x3e\x2e\x1b\x5e\xec\xde\xef\x7f\xc2\x7c\x90\xf1" +
                 b"\xfa\x14\x8c\xa1\xc2\x5c\x2f\xe6\x25\x2a\x57\x7c\x4b\x27\xf2\x56" +
                 b"\xe1\x72\xe9\xd5\x3b\x22\xb4\x62\x8b\x8b\xb7\x2a\xf5\xd7\x9b\x25" +
                 b"\xd9\xf9\xee\x0a\x1a\x65\xab\x98\x0d\x71\xa2\x85\x06\x49\x67\x89" )

    data      = (b"\x05\x12\xc7\x06\x06\x88\xab\xf8\xf1\xeb\xb2\xd6\x66\x00\x56\x66" +
                 b"\xa3\xde\x34\x1a\x2c\x81\xf6\x6d\xe2\xb0\x8f\xfb\xb8\xa8\x27\x4e" +
                 b"\x1c"                                                             )

    assert XEdDSA25519(mont_pub = mont_pub).verify(data, signature)
