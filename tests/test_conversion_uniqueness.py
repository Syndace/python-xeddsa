import secrets

import xeddsa


__all__ = [  # pylint: disable=unused-variable
    "test_conversion_uniqueness"
]

NUM_KEYS = 8192


def test_conversion_uniqueness() -> None:
    """
    Test conversion uniqueness between public key formats.
    """

    # Test on a set of different keys
    for _ in range(NUM_KEYS):
        # Generate a Curve25519 key pair (the private key is not used).
        curve_priv = secrets.token_bytes(32)
        curve_pub_original = xeddsa.priv_to_curve25519_pub(curve_priv)

        # Convert the Curve25519 public key to an Ed25519 public key
        ed_pub_converted = xeddsa.curve25519_pub_to_ed25519_pub(curve_pub_original, False)

        # Convert the Ed25519 public key back into a Curve25519 public key
        curve_pub_converted = xeddsa.ed25519_pub_to_curve25519_pub(ed_pub_converted)

        # Check whether the converted Curve25519 public key is equal to the original
        assert curve_pub_original == curve_pub_converted

        # Generate an Ed25519 key pair (the private key is not used).
        ed_priv = secrets.token_bytes(32)
        ed_pub_original = xeddsa.priv_to_ed25519_pub(ed_priv)

        # Convert the Ed25519 public key to a Curve25519 public key
        curve_pub_converted = xeddsa.ed25519_pub_to_curve25519_pub(ed_pub_original)

        # Convert the Curve25519 public key back into an Ed25519 public key. Set the sign accordingly.
        original_sign = bool(ed_pub_original[31] & 0x80)
        ed_pub_converted = xeddsa.curve25519_pub_to_ed25519_pub(curve_pub_converted, original_sign)

        # Check whether the converted Ed25519 public key is equal to the original
        assert ed_pub_original == ed_pub_converted
