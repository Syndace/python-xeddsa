from xeddsa import XEdDSA25519

def test_generates_key_pair():
    x = XEdDSA25519()
    assert x.mont_priv is not None
    assert x.mont_pub  is not None

def test_derives_public_key():
    x = XEdDSA25519(mont_priv=XEdDSA25519.generate_mont_priv())
    assert x.mont_priv is not None
    assert x.mont_pub  is not None

def test_missing_private_key():
    x = XEdDSA25519(mont_pub=XEdDSA25519.mont_pub_from_mont_priv(XEdDSA25519.generate_mont_priv()))
    assert x.mont_priv is     None
    assert x.mont_pub  is not None
