# This import from future (theoretically) enables sphinx_autodoc_typehints to handle type aliases better
from __future__ import annotations  # pylint: disable=unused-variable

import secrets
from typing import Optional

try:
    from _libxeddsa import ffi, lib
except ImportError:
    from .libxeddsa_emscripten import ffi, lib  # type: ignore[assignment]


__all__ = [  # pylint: disable=unused-variable
    "Priv", "PRIV_SIZE",
    "Seed", "SEED_SIZE",
    "Curve25519Pub", "CURVE_25519_PUB_SIZE",
    "Ed25519Pub", "ED_25519_PUB_SIZE",
    "Ed25519Signature", "ED_25519_SIGNATURE_SIZE",
    "Nonce", "NONCE_SIZE",
    "SharedSecret", "SHARED_SECRET_SIZE",

    "XEdDSAException",

    "ed25519_priv_sign",
    "ed25519_seed_sign",
    "ed25519_verify",

    "curve25519_pub_to_ed25519_pub",
    "ed25519_pub_to_curve25519_pub",

    "priv_to_curve25519_pub",
    "priv_to_ed25519_pub",
    "seed_to_ed25519_pub",

    "priv_force_sign",
    "seed_to_priv",

    "x25519"
]

Priv = bytes
PRIV_SIZE = 32
PRIV_FFI = f"uint8_t[{PRIV_SIZE}]"

Seed = bytes
SEED_SIZE = 32
SEED_FFI = f"uint8_t[{SEED_SIZE}]"

Curve25519Pub = bytes
CURVE_25519_PUB_SIZE = 32
CURVE_25519_PUB_FFI = f"uint8_t[{CURVE_25519_PUB_SIZE}]"

Ed25519Pub = bytes
ED_25519_PUB_SIZE = 32
ED_25519_PUB_FFI = f"uint8_t[{ED_25519_PUB_SIZE}]"

Ed25519Signature = bytes
ED_25519_SIGNATURE_SIZE = 64
ED_25519_SIGNATURE_FFI = f"uint8_t[{ED_25519_SIGNATURE_SIZE}]"

Nonce = bytes
NONCE_SIZE = 64
NONCE_FFI = f"uint8_t[{NONCE_SIZE}]"

SharedSecret = bytes
SHARED_SECRET_SIZE = 32
SHARED_SECRET_FFI = f"uint8_t[{SHARED_SECRET_SIZE}]"


class XEdDSAException(Exception):
    """
    Exception raised in case of critical security errors.
    """


def ed25519_priv_sign(priv: Priv, msg: bytes, nonce: Optional[Nonce] = None) -> Ed25519Signature:
    """
    Sign a message using a Curve25519/Ed25519 private key.

    Args:
        priv: The Curve25519/Ed25519 private key to sign with.
        msg: The message to sign.
        nonce: 64 bytes of secure random data. If `None` is passed, the nonce is generated for you.

    Returns:
        An Ed25519-compatible signature of `msg`.
    """

    if len(priv) != PRIV_SIZE:
        raise ValueError(f"Expected size of the private key in bytes: {PRIV_SIZE} (PRIV_SIZE)")

    if nonce is None:
        nonce = secrets.token_bytes(NONCE_SIZE)

    if len(nonce) != NONCE_SIZE:
        raise ValueError(f"Expected size of the nonce in bytes: {NONCE_SIZE} (NONCE_SIZE")

    sig_ffi = ffi.new(ED_25519_SIGNATURE_FFI)
    priv_ffi = ffi.new(PRIV_FFI, priv)
    msg_ffi = ffi.new("uint8_t[]", msg)
    msg_size = len(msg)
    nonce_ffi = ffi.new(NONCE_FFI, nonce)

    lib.ed25519_priv_sign(sig_ffi, priv_ffi, msg_ffi, msg_size, nonce_ffi)

    return bytes(sig_ffi)


def ed25519_seed_sign(seed: Seed, msg: bytes) -> Ed25519Signature:
    """
    Sign a message using a Curve25519/Ed25519 seed.

    Args:
        seed: The Curve25519/Ed25519 seed to sign with.
        msg: The message to sign.

    Returns:
        An Ed25519-compatible signature of `msg`.
    """

    if len(seed) != SEED_SIZE:
        raise ValueError(f"Expected size of the seed in bytes: {SEED_SIZE} (SEED_SIZE)")

    sig_ffi = ffi.new(ED_25519_SIGNATURE_FFI)
    seed_ffi = ffi.new(SEED_FFI, seed)
    msg_ffi = ffi.new("uint8_t[]", msg)
    msg_size = len(msg)

    lib.ed25519_seed_sign(sig_ffi, seed_ffi, msg_ffi, msg_size)

    return bytes(sig_ffi)


def ed25519_verify(sig: Ed25519Signature, ed25519_pub: Ed25519Pub, msg: bytes) -> bool:
    """
    Verify an Ed25519 signature.

    Args:
        sig: An Ed25519-compatible signature of `msg`.
        ed25519_pub: The Ed25519 public key to verify the signature with.
        msg: The message.

    Returns:
        Whether the signature verification was successful.
    """

    if len(sig) != ED_25519_SIGNATURE_SIZE:
        raise ValueError(
            f"Expected size of the signature in bytes: {ED_25519_SIGNATURE_SIZE} (ED_25519_SIGNATURE_SIZE)"
        )

    if len(ed25519_pub) != ED_25519_PUB_SIZE:
        raise ValueError(
            f"Expected size of the Ed25519 public key in bytes: {ED_25519_PUB_SIZE} (ED_25519_PUB_SIZE)"
        )

    sig_ffi = ffi.new(ED_25519_SIGNATURE_FFI, sig)
    ed25519_pub_ffi = ffi.new(ED_25519_PUB_FFI, ed25519_pub)
    msg_ffi = ffi.new("uint8_t[]", msg)
    msg_size = len(msg)

    return lib.ed25519_verify(sig_ffi, ed25519_pub_ffi, msg_ffi, msg_size) == 0


def curve25519_pub_to_ed25519_pub(curve25519_pub: Curve25519Pub, set_sign_bit: bool) -> Ed25519Pub:
    """
    Convert a Curve25519 public key into an Ed25519 public key.

    Args:
        curve25519_pub: The Curve25519 public key to convert into its Ed25519 equivalent.
        set_sign_bit: Whether to set the sign bit of the output Ed25519 public key.

    Returns:
        The Ed25519 public key corresponding to the Curve25519 public key.
    """

    if len(curve25519_pub) != CURVE_25519_PUB_SIZE:
        raise ValueError(
            f"Expected size of the Curve25519 public key in bytes: {CURVE_25519_PUB_SIZE}"
            " (CURVE_25519_PUB_SIZE)"
        )

    ed25519_pub_ffi = ffi.new(ED_25519_PUB_FFI)
    curve25519_pub_ffi = ffi.new(CURVE_25519_PUB_FFI, curve25519_pub)

    lib.curve25519_pub_to_ed25519_pub(ed25519_pub_ffi, curve25519_pub_ffi, set_sign_bit)

    return bytes(ed25519_pub_ffi)


def ed25519_pub_to_curve25519_pub(ed25519_pub: Ed25519Pub) -> Curve25519Pub:
    """
    Convert an Ed25519 public key into a Curve25519 public key. Re-export of libsodiums/ref10s
    `crypto_sign_ed25519_pk_to_curve25519` function for convenience.

    Args:
        ed25519_pub: The Ed25519 public key to convert into its Curve25519 equivalent.

    Returns:
        The Curve25519 public key corresponding to the Ed25519 public key.

    Raises:
        XEdDSAException: if the public key was rejected due to suboptimal security propierties.
    """

    if len(ed25519_pub) != ED_25519_PUB_SIZE:
        raise ValueError(
            f"Expected size of the Ed25519 public key in bytes: {ED_25519_PUB_SIZE} (ED_25519_PUB_SIZE)"
        )

    curve25519_pub_ffi = ffi.new(CURVE_25519_PUB_FFI)
    ed25519_pub_ffi = ffi.new(ED_25519_PUB_FFI, ed25519_pub)

    if lib.ed25519_pub_to_curve25519_pub(curve25519_pub_ffi, ed25519_pub_ffi) != 0:
        raise XEdDSAException("Ed25519 public key rejected due to suboptimal security properties.")

    return bytes(curve25519_pub_ffi)


def priv_to_curve25519_pub(priv: Priv) -> Curve25519Pub:
    """
    Derive the Curve25519 public key from a Curve25519/Ed25519 private key.

    Args:
        priv: The Curve25519/Ed25519 private key.

    Returns:
        The Curve25519 public key.
    """

    if len(priv) != PRIV_SIZE:
        raise ValueError(f"Expected size of the private key in bytes: {PRIV_SIZE} (PRIV_SIZE)")

    curve25519_pub_ffi = ffi.new(CURVE_25519_PUB_FFI)
    priv_ffi = ffi.new(PRIV_FFI, priv)

    lib.priv_to_curve25519_pub(curve25519_pub_ffi, priv_ffi)

    return bytes(curve25519_pub_ffi)


def priv_to_ed25519_pub(priv: Priv) -> Ed25519Pub:
    """
    Derive the Ed25519 public key from a Curve25519/Ed25519 private key.

    Args:
        priv: The Curve25519/Ed25519 private key.

    Returns:
        The Ed25519 public key.
    """

    if len(priv) != PRIV_SIZE:
        raise ValueError(f"Expected size of the private key in bytes: {PRIV_SIZE} (PRIV_SIZE)")

    ed25519_pub_ffi = ffi.new(ED_25519_PUB_FFI)
    priv_ffi = ffi.new(PRIV_FFI, priv)

    lib.priv_to_ed25519_pub(ed25519_pub_ffi, priv_ffi)

    return bytes(ed25519_pub_ffi)


def seed_to_ed25519_pub(seed: Seed) -> Ed25519Pub:
    """
    Derive the Ed25519 public key from a Curve25519/Ed25519 seed.

    Args:
        seed: The Curve25519/Ed25519 seed.

    Returns:
        The Ed25519 public key.
    """

    if len(seed) != SEED_SIZE:
        raise ValueError(f"Expected size of the seed in bytes: {SEED_SIZE} (SEED_SIZE)")

    ed25519_pub_ffi = ffi.new(ED_25519_PUB_FFI)
    seed_ffi = ffi.new(SEED_FFI, seed)

    lib.seed_to_ed25519_pub(ed25519_pub_ffi, seed_ffi)

    return bytes(ed25519_pub_ffi)


def priv_force_sign(priv: Priv, set_sign_bit: bool) -> Priv:
    """
    Negate a Curve25519/Ed25519 private key if necessary, such that the corresponding Ed25519 public key has
    the sign bit set (or not set) as requested.

    Args:
        priv: The original Curve25519/Ed25519 private key.
        set_sign_bit: Whether the goal is for the sign bit to be set on the Ed25519 public key corresponding
            to the adjusted Curve25519/Ed25519 private key.

    Returns:
        The adjusted Curve25519/Ed25519 private key.
    """

    if len(priv) != PRIV_SIZE:
        raise ValueError(f"Expected size of the private key in bytes: {PRIV_SIZE} (PRIV_SIZE)")

    priv_out_ffi = ffi.new(PRIV_FFI)
    priv_in_ffi = ffi.new(PRIV_FFI, priv)

    lib.priv_force_sign(priv_out_ffi, priv_in_ffi, set_sign_bit)

    return bytes(priv_out_ffi)


def seed_to_priv(seed: Seed) -> Priv:
    """
    Derive the Curve25519/Ed25519 private key from a Curve25519/Ed25519 seed. Re-export of libsodiums/ref10s
    `crypto_sign_ed25519_sk_to_curve25519` function for convenience.

    Args:
        seed: The Curve25519/Ed25519 seed.

    Returns:
        The Curve25519/Ed25519 private key derived from the seed.
    """

    if len(seed) != SEED_SIZE:
        raise ValueError(f"Expected size of the seed in bytes: {SEED_SIZE} (SEED_SIZE)")

    priv_ffi = ffi.new(PRIV_FFI)
    seed_ffi = ffi.new(SEED_FFI, seed)

    lib.seed_to_priv(priv_ffi, seed_ffi)

    return bytes(priv_ffi)


def x25519(priv: Priv, curve25519_pub: Curve25519Pub) -> SharedSecret:
    """
    Perform Diffie-Hellman key agreement on Curve25519, also known as X25519.

    Args:
        priv: The private key partaking in the key agreement.
        curve25519_pub: The public key partaking in the key agreement.

    Returns:
        The shared secret.

    Raises:
        XEdDSAException: if the public key was rejected due to suboptimal security propierties or if the
            shared secret consists of only zeros
    """

    if len(priv) != PRIV_SIZE:
        raise ValueError(f"Expected size of the private key in bytes: {PRIV_SIZE} (PRIV_SIZE)")

    if len(curve25519_pub) != CURVE_25519_PUB_SIZE:
        raise ValueError(
            f"Expected size of the Curve25519 public key in bytes: {CURVE_25519_PUB_SIZE}"
            " (CURVE_25519_PUB_SIZE)"
        )

    shared_secret_ffi = ffi.new(SHARED_SECRET_FFI)
    priv_ffi = ffi.new(PRIV_FFI, priv)
    curve25519_pub_ffi = ffi.new(CURVE_25519_PUB_FFI, curve25519_pub)

    if lib.x25519(shared_secret_ffi, priv_ffi, curve25519_pub_ffi) != 0:
        raise XEdDSAException(
            "Key agreement failed, either due to suboptimal security properties of the public key, or due to"
            " the shared secret consisting of only zeros."
        )

    return bytes(shared_secret_ffi)


if not 2 <= lib.XEDDSA_VERSION_MAJOR < 3:
    raise Exception(
        "Wrong version of libxeddsa bound. Expected >=2,<3, got"
        f" {lib.XEDDSA_VERSION_MAJOR}.{lib.XEDDSA_VERSION_MINOR}.{lib.XEDDSA_VERSION_REVISION}"
    )

if lib.xeddsa_init() < 0:
    raise Exception("libxeddsa couldn't be initialized.")
