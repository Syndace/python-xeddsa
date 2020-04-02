from xeddsa import XEdDSA25519

def test_generates_key_pair() -> None:
    instance = XEdDSA25519()
    assert instance.mont_priv is not None
    assert instance.mont_pub  is not None

def test_derives_public_key() -> None:
    instance = XEdDSA25519(mont_priv=XEdDSA25519.generate_mont_priv())
    assert instance.mont_priv is not None
    assert instance.mont_pub  is not None

def test_missing_private_key() -> None:
    instance = XEdDSA25519(mont_pub=XEdDSA25519.mont_pub_from_mont_priv(XEdDSA25519.generate_mont_priv()))
    assert instance.mont_priv is     None
    assert instance.mont_pub  is not None
