import random

import xeddsa


__all__ = [  # pylint: disable=unused-variable
    "test_signing"
]

NUM_MESSAGES = 64
NUM_KEY_PAIRS = 64


def test_signing() -> None:
    """
    Test signing/verification flows for Curve25519, Ed25519 and seed-based key pairs.
    """

    # Test on a set of different messages
    for _ in range(NUM_MESSAGES):
        # Fill the message with random bytes. Randomize the size of the message.
        msg = random.randbytes(random.randrange(0, 65535))

        # Test each message on a set of different key pairs
        for _ in range(NUM_KEY_PAIRS):
            # Generate a Curve25519 key pair. WARNING: Do not use random.randbytes for private keys!
            curve_priv = random.randbytes(32)
            curve_pub = xeddsa.priv_to_curve25519_pub(curve_priv)

            # Adjust the private key such that the sign of the derived Ed25519 public key is zero
            priv = xeddsa.priv_force_sign(curve_priv, False)

            # Sign the message using the Curve25519 private key
            sig = xeddsa.ed25519_priv_sign(priv, msg)

            # Convert the Curve25519 public key to an Ed25519 public key
            ed_pub = xeddsa.curve25519_pub_to_ed25519_pub(curve_pub, False)

            # Verify the message using the converted public key.
            assert xeddsa.ed25519_verify(sig, ed_pub, msg)

            # Convert the Curve25519 public key to an Ed25519 public key, intentionally choosing the wrong
            # sign
            ed_pub = xeddsa.curve25519_pub_to_ed25519_pub(curve_pub, True)

            # Verify the message using the converted public key.
            assert not xeddsa.ed25519_verify(sig, ed_pub, msg)

            # Adjust the private key such that the sign of the derived Ed25519 public key is one
            priv = xeddsa.priv_force_sign(curve_priv, True)

            # Sign the message using the Curve25519 private key
            sig = xeddsa.ed25519_priv_sign(priv, msg)

            # Convert the Curve25519 public key to an Ed25519 public key
            ed_pub = xeddsa.curve25519_pub_to_ed25519_pub(curve_pub, True)

            # Verify the message using the converted public key.
            assert xeddsa.ed25519_verify(sig, ed_pub, msg)

            # Convert the Curve25519 public key to an Ed25519 public key, intentionally choosing the wrong
            # sign
            ed_pub = xeddsa.curve25519_pub_to_ed25519_pub(curve_pub, False)

            # Verify the message using the converted public key.
            assert not xeddsa.ed25519_verify(sig, ed_pub, msg)

            # Generate an Ed25519 key pair. WARNING: Do not use random.randbytes for seeds!
            ed_seed = random.randbytes(32)
            ed_pub = xeddsa.seed_to_ed25519_pub(ed_seed)

            # Sign the message normally
            sig = xeddsa.ed25519_seed_sign(ed_seed, msg)

            # Verify the message normally
            assert xeddsa.ed25519_verify(sig, ed_pub, msg)
