from ctypes import *
import struct

libsodium = cdll.LoadLibrary("/usr/local/lib/libsodium.so")

crypto_scalarmult_ed25519_type        = c_byte * libsodium.crypto_scalarmult_ed25519_bytes()
crypto_scalarmult_ed25519_scalar_type = c_byte * libsodium.crypto_scalarmult_ed25519_scalarbytes()

def crypto_scalarmult_ed25519_base(scalar):
    scalar = crypto_scalarmult_ed25519_scalar_type(*scalar)
    result = crypto_scalarmult_ed25519_type()

    libsodium.crypto_scalarmult_ed25519_base(result, scalar)

    return result

def mont_priv_to_ed_pair(mont_priv):
    # Get the twisted edwards public key, including the sign bit
    ed_pub = crypto_scalarmult_ed25519_base(mont_priv)

    # Save the sign bit for later
    sign_bit = (ed_pub[31] & 0x80) >> 7

    # Force the sign bit to zero
    ed_pub[31] &= 0x7F

    # Prepare the negated montgomery private key
    mont_priv_neg = neg(mont_priv)

    # Get the correct private key based on the sign stored above
    ed_priv = either(mont_priv, mont_priv_neg, sign_bit)

    return to_byte_array(ed_priv), to_byte_array(ed_pub)

def to_byte_array(array):
    return bytes(bytearray(array))

def bytes_to_int(bytes):
    value = 0

    for i in range(32):
        value |= bytes[i] << (i * 8)

    return value

def int_to_bytes(value):
    result = []

    for i in range(32):
        result.append(value & 0xFF)
        value >>= 8

    return result

p = pow(2, 255) - 19

def neg(a):
    return int_to_bytes(pow(bytes_to_int(a), p - 2, p))

def either(a, b, condition):
    # Create an 8 bit mask of either all zeros or all ones
    condition = (condition << 0 | condition << 1 |
                 condition << 2 | condition << 3 |
                 condition << 4 | condition << 5 |
                 condition << 6 | condition << 7 )

    tmp = []

    # Mix (xor) together a and b
    for x, y in zip(a, b):
        tmp.append(x ^ y)

    # Either keep the mixed values as they are or reset them to zeros
    for i in range(len(tmp)):
        tmp[i] &= condition

    result = []

    # Build the resulting values:
    # y contains either a ^ b bytes or zeros, x contains bytes of a.
    # If y contains zeros, the result will be a.
    # Otherwise, a ^ a ^ b will get calculated which results in b.
    for x, y in zip(a, tmp):
        result.append(x ^ y)

    return result
