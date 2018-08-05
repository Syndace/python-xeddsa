import os

from xeddsa.implementations import XEdDSA25519

def test_types():
    message = os.urandom(100)

    mont_priv = XEdDSA25519.generate_mont_priv()
    mont_pub  = XEdDSA25519.mont_pub_from_mont_priv(mont_priv)

    assert isinstance(mont_priv, bytes)
    assert isinstance(mont_pub,  bytes)

    signing_xeddsa   = XEdDSA25519(mont_priv = mont_priv)
    verifying_xeddsa = XEdDSA25519(mont_pub  = mont_pub)

    signature = signing_xeddsa.sign(message)

    assert isinstance(signature, bytes)

    assert verifying_xeddsa.verify(message, signature)

    ed_priv, ed_pub_a = XEdDSA25519.mont_priv_to_ed_pair(mont_priv)
    ed_pub_b = XEdDSA25519.mont_pub_to_ed_pub(mont_pub)

    assert isinstance(ed_pub_a, bytes)
    assert isinstance(ed_priv,  bytes)
    assert isinstance(ed_pub_b, bytes)

    assert ed_pub_a == ed_pub_b
