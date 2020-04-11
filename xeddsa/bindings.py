from _libxeddsa import ffi, lib

Curve25519Priv = bytes
CURVE_25519_PRIV_SIZE = 32
CURVE_25519_PRIV_FFI  = "uint8_t[{}]".format(CURVE_25519_PRIV_SIZE)

Curve25519Pub = bytes
CURVE_25519_PUB_SIZE = 32
CURVE_25519_PUB_FFI  = "uint8_t[{}]".format(CURVE_25519_PUB_SIZE)

Ed25519Pub = bytes
ED_25519_PUB_SIZE = 32
ED_25519_PUB_FFI  = "uint8_t[{}]".format(ED_25519_PUB_SIZE)

Ed25519Signature = bytes
ED_25519_SIGNATURE_SIZE = 64
ED_25519_SIGNATURE_FFI = "uint8_t[{}]".format(ED_25519_SIGNATURE_SIZE)

Nonce = bytes
NONCE_SIZE = 64
NONCE_FFI  = "uint8_t[{}]".format(NONCE_SIZE)

def xeddsa_init() -> int:
    """
    Initializes libxeddsa and its dependencies. Has to be called at least once before using
    :func:`curve25519_sign` or :func:`curve25519_pub_to_ed25519_pub`. Can be called multiple times, even from
    different threads.

    Returns:
        0 if the library was initialized, 1 if the library was already initialized and -1 in case of an error.
    """

    return lib.xeddsa_init()

def curve25519_sign(curve25519_priv: Curve25519Priv, msg: bytes, nonce: Nonce) -> Ed25519Signature:
    """
    Sign a message using a Curve25519 private key.

    Args:
        curve25519_priv: The Curve25519 private key to sign `msg` with. The little-endian encoding of the u
            coordinate as per `RFC 7748 <https://tools.ietf.org/html/rfc7748#page-4>`__ (on page 4).
        msg: The message to sign.
        nonce: 64 bytes of secure random data.

    Returns:
        An Ed25519-compatible signature that validates `msg` with the Ed25519 public key corresponding to this
        Curve25519 private key, as calculated by :func:`curve25519_pub_to_ed25519_pub`. The signature is 64
        bytes long and follows the byte format defined in
        `RFC 8032 <https://tools.ietf.org/html/rfc8032#page-8>`__ (on page 8).
    """

    sig_ffi = ffi.new(ED_25519_SIGNATURE_FFI)
    curve25519_priv_ffi = ffi.new(CURVE_25519_PRIV_FFI, curve25519_priv)
    msg_ffi = ffi.new("uint8_t[]", msg)
    msg_size = len(msg)
    nonce_ffi = ffi.new(NONCE_FFI, nonce)

    lib.curve25519_sign(sig_ffi, curve25519_priv_ffi, msg_ffi, msg_size, nonce_ffi)

    return bytes(sig_ffi)

def curve25519_pub_to_ed25519_pub(curve25519_pub: Curve25519Pub) -> Ed25519Pub:
    """
    Convert a Curve25519 public key into an Ed25519 public key, which validates signatures created by using
    :func:`curve25519_sign` with the corresponding Curve25519 private key.

    Args:
        curve25519_pub: The Curve25519 public key to convert into its Ed25519 equivalent. The little-endian
            encoding of the u coordinate as per `RFC 7748 <https://tools.ietf.org/html/rfc7748#page-4>`__ (on
            page 4).

    Returns:
        The Ed25519 public key corresponding to the Curve25519 public key. The little-endian encoding of the y
        coordinate (32 bytes) with the sign bit of the x coordinate stored in the most significant bit as per
        `RFC 8032 <https://tools.ietf.org/html/rfc8032#page-7>`__ (on page 7).
    """

    ed25519_pub_ffi    = ffi.new(ED_25519_PUB_FFI)
    curve25519_pub_ffi = ffi.new(CURVE_25519_PUB_FFI, curve25519_pub)

    lib.curve25519_pub_to_ed25519_pub(ed25519_pub_ffi, curve25519_pub_ffi)

    return bytes(ed25519_pub_ffi)

if xeddsa_init() < 0:
    raise Exception("libxeddsa couldn't be initialized.")
