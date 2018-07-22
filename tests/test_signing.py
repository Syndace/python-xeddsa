from __future__ import print_function

import os
import pytest

from xeddsa.implementations import XEdDSA25519

from test_conversion import montgomery_private_keys

def test_signing():
    message = os.urandom(100)
    nonce   = os.urandom(64)

    tests = 0
    successes = 0

    for mont_priv in montgomery_private_keys:
        xeddsa = XEdDSA25519(decryption_key = mont_priv)

        signature = xeddsa.sign(message, nonce)

        assert xeddsa.verify(message, signature)
