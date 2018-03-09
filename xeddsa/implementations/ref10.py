from ctypes import *

ref10 = cdll.LoadLibrary("libref10.so")

###############################################################################
# Utilities                                                                   #
###############################################################################
def wrap(bytes, ctype):
    if not isinstance(bytes, ctype):
        return ctype(*bytes)
    return bytes

###############################################################################
# fe.h                                                                        #
###############################################################################
fe = c_int32 * 10
fe_bytes = c_uint8 * 32

def fe_frombytes(fe_bytes_BYTES):
    fe_bytes_BYTES = wrap(fe_bytes_BYTES, fe_bytes)

    result = fe()
    ref10.crypto_sign_ed25519_ref10_fe_frombytes(result, fe_bytes_BYTES)
    return result

def fe_tobytes(fe_FE):
    result = fe_bytes()
    ref10.crypto_sign_ed25519_ref10_fe_tobytes(result, fe_FE)
    return list(result)

def fe_1():
    result = fe()
    ref10.crypto_sign_ed25519_ref10_fe_1(result)
    return result

def fe_add(fe_ADDEND_A, fe_ADDEND_B):
    result = fe()
    ref10.crypto_sign_ed25519_ref10_fe_add(result, fe_ADDEND_A, fe_ADDEND_B)
    return result

def fe_sub(fe_MINUEND, fe_SUBTRAHEND):
    result = fe()
    ref10.crypto_sign_ed25519_ref10_fe_sub(result, fe_MINUEND, fe_SUBTRAHEND)
    return result

def fe_mul(fe_MULTIPLICAND, fe_MULTIPLIER):
    result = fe()
    ref10.crypto_sign_ed25519_ref10_fe_mul(result, fe_MULTIPLICAND, fe_MULTIPLIER)
    return result

def fe_invert(fe_FE):
    result = fe()
    ref10.crypto_sign_ed25519_ref10_fe_invert(result, fe_FE)
    return result

###############################################################################
# ge.h                                                                        #
###############################################################################
class ge_p3(Structure):
    _fields_ = [("X", fe),
                ("Y", fe),
                ("Z", fe),
                ("T", fe)]

ge_p3_bytes = c_uint8 * 32

def ge_p3_tobytes(ge_p3_POINT):
    result = ge_p3_bytes()
    ref10.crypto_sign_ed25519_ref10_ge_p3_tobytes(result, byref(ge_p3_POINT))
    return list(result)

scalar_bytes = c_uint8 * 32

def ge_scalarmult_base(scalar_bytes_SCALAR):
    scalar_bytes_SCALAR = wrap(scalar_bytes_SCALAR, scalar_bytes)

    result = ge_p3()
    ref10.crypto_sign_ed25519_ref10_ge_scalarmult_base(byref(result), scalar_bytes_SCALAR)
    return result

###############################################################################
# sc.h                                                                        #
###############################################################################
sc_bytes        = c_uint8 * 32
sc_reduce_bytes = c_uint8 * 64

def sc_reduce(sc_reduce_bytes_SC):
    sc_reduce_bytes_SC = wrap(sc_reduce_bytes_SC, sc_reduce_bytes)

    ref10.crypto_sign_ed25519_ref10_sc_reduce(sc_reduce_bytes_SC)

    return list(sc_reduce_bytes_SC)[:32]

def sc_muladd(sc_bytes_MULTIPLICAND, sc_bytes_MULTIPLIER, sc_bytes_ADDEND):
    sc_bytes_MULTIPLICAND = wrap(sc_bytes_MULTIPLICAND, sc_bytes)
    sc_bytes_MULTIPLIER   = wrap(sc_bytes_MULTIPLIER, sc_bytes)
    sc_bytes_ADDEND       = wrap(sc_bytes_ADDEND, sc_bytes)

    result = sc_bytes()
    ref10.crypto_sign_ed25519_ref10_sc_muladd(result, sc_bytes_MULTIPLICAND, sc_bytes_MULTIPLIER, sc_bytes_ADDEND)
    return list(result)

###############################################################################
# XEdDSA additions                                                            #
###############################################################################
sc_bytes_BASE_POINT_ORDER_MINUS_ONE = sc_bytes(*[
    0xEC, 0xD3, 0xF5, 0x5C, 0x1A, 0x63, 0x12, 0x58,
    0xD6, 0x9C, 0xF7, 0xA2, 0xDE, 0xF9, 0xDE, 0x14,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10
])

sc_bytes_ZERO = sc_bytes(*([ 0x00 ] * 32))

def sc_neg(sc_bytes_BYTES):
    return sc_muladd(sc_bytes_BASE_POINT_ORDER_MINUS_ONE, sc_bytes_BYTES, sc_bytes_ZERO)

def sc_cmov(sc_bytes_A, sc_bytes_B, byte_CONDITION):
    # Make sure the condition is either a one or a zero
    condition = (byte_CONDITION & 0xFF) != 0x00

    # Create an eight bit mask for the condition, either all ones or all zeros
    condition_mask = ( condition << 0 |
                       condition << 1 |
                       condition << 2 |
                       condition << 3 |
                       condition << 4 |
                       condition << 5 |
                       condition << 6 |
                       condition << 7 )

    for i in range(32):
        # Mix together the two scalars a and b by xor'ing them
        # tmp = a ^ b
        tmp = sc_bytes_A[i] ^ sc_bytes_B[i]

        # Now, apply the condition mask to the temporary result, which creates either of:
        # - tmp = (a ^ b) & 0xFF = a ^ b, if the condition is true
        # - tmp = (a ^ b) & 0x00 = 0    , if the condition is false
        tmp &= condition_mask

        # Finally, xor the temporary result with the bytes of a.
        # This results in either of the following based on the condition:
        # - a ^ tmp = a ^ (a ^ b) = b, if the condition is true
        # - a ^ tmp = a ^ (0    ) = a, if the condition is false
        sc_bytes_A[i] ^= tmp
