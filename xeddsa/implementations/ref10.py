import _crypto_sign

###############################################################################
# fe.h                                                                        #
###############################################################################
def fe_bytes(fe_bytes_BYTES = None):
    if isinstance(fe_bytes_BYTES, _crypto_sign.ffi.CData):
        return fe_bytes_BYTES
    else:
        return _crypto_sign.ffi.new("uint8_t[32]", fe_bytes_BYTES)

def fe(fe_FE = None):
    if isinstance(fe_FE, _crypto_sign.ffi.CData):
        return fe_FE
    else:
        return _crypto_sign.ffi.new("int32_t[10]", fe_FE)

def fe_frombytes(fe_bytes_BYTES):
    result = fe()
    _crypto_sign.lib.crypto_sign_ed25519_ref10_fe_frombytes(result, fe_bytes(fe_bytes_BYTES))
    return result

def fe_tobytes(fe_FE):
    result = fe_bytes()
    _crypto_sign.lib.crypto_sign_ed25519_ref10_fe_tobytes(result, fe(fe_FE))
    return result

def fe_1():
    result = fe()
    _crypto_sign.lib.crypto_sign_ed25519_ref10_fe_1(result)
    return result

def fe_add(fe_ADDEND_A, fe_ADDEND_B):
    result = fe()
    _crypto_sign.lib.crypto_sign_ed25519_ref10_fe_add(result, fe(fe_ADDEND_A), fe(fe_ADDEND_B))
    return result

def fe_sub(fe_MINUEND, fe_SUBTRAHEND):
    result = fe()
    _crypto_sign.lib.crypto_sign_ed25519_ref10_fe_sub(result, fe(fe_MINUEND), fe(fe_SUBTRAHEND))
    return result

def fe_mul(fe_MULTIPLICAND, fe_MULTIPLIER):
    result = fe()
    _crypto_sign.lib.crypto_sign_ed25519_ref10_fe_mul(result, fe(fe_MULTIPLICAND), fe(fe_MULTIPLIER))
    return result

def fe_invert(fe_FE):
    result = fe()
    _crypto_sign.lib.crypto_sign_ed25519_ref10_fe_invert(result, fe(fe_FE))
    return result

###############################################################################
# ge.h                                                                        #
###############################################################################
class ge_p3(object):
    def __init__(self, ge_p3_POINT = None):
        self.__point = ge_p3_POINT

    @classmethod
    def empty(cls):
        return cls(_crypto_sign.ffi.new("ge_p3 *"))

    @property
    def point(self):
        return self.__point

def ge_p3_bytes(ge_p3_bytes_BYTES = None):
    if isinstance(ge_p3_bytes_BYTES, _crypto_sign.ffi.CData):
        return ge_p3_bytes_BYTES
    else:
        return _crypto_sign.ffi.new("uint8_t[32]", ge_p3_bytes_BYTES)

def ge_p3_tobytes(ge_p3_POINT):
    result = ge_p3_bytes()
    _crypto_sign.lib.crypto_sign_ed25519_ref10_ge_p3_tobytes(result, ge_p3_POINT.point)
    return result

def scalar_bytes(scalar_bytes_SCALAR = None):
    if isinstance(scalar_bytes_SCALAR, _crypto_sign.ffi.CData):
        return scalar_bytes_SCALAR
    else:
        return _crypto_sign.ffi.new("uint8_t[32]", scalar_bytes_SCALAR)

def ge_scalarmult_base(scalar_bytes_SCALAR):
    result = ge_p3.empty()
    _crypto_sign.lib.crypto_sign_ed25519_ref10_ge_scalarmult_base(result.point, scalar_bytes(scalar_bytes_SCALAR))
    return result

###############################################################################
# sc.h                                                                        #
###############################################################################
def sc_bytes(sc_bytes_BYTES = None):
    if isinstance(sc_bytes_BYTES, _crypto_sign.ffi.CData):
        return sc_bytes_BYTES
    else:
        return _crypto_sign.ffi.new("uint8_t[32]", sc_bytes_BYTES)

def sc_reduce_bytes(sc_reduce_bytes_BYTES):
    if isinstance(sc_reduce_bytes_BYTES, _crypto_sign.ffi.CData):
        return sc_reduce_bytes_BYTES
    else:
        return _crypto_sign.ffi.new("uint8_t[64]", sc_reduce_bytes_BYTES)

def sc_reduce(sc_reduce_bytes_SC):
    sc_reduce_bytes_SC = sc_reduce_bytes(sc_reduce_bytes_SC)
    _crypto_sign.lib.crypto_sign_ed25519_ref10_sc_reduce(sc_reduce_bytes_SC)
    return sc_bytes(list(sc_reduce_bytes_SC)[:32])

def sc_muladd(sc_bytes_MULTIPLICAND, sc_bytes_MULTIPLIER, sc_bytes_ADDEND):
    result = sc_bytes()
    _crypto_sign.lib.crypto_sign_ed25519_ref10_sc_muladd(result, sc_bytes(sc_bytes_MULTIPLICAND), sc_bytes(sc_bytes_MULTIPLIER), sc_bytes(sc_bytes_ADDEND))
    return result

###############################################################################
# XEdDSA additions                                                            #
###############################################################################
sc_bytes_BASE_POINT_ORDER_MINUS_ONE = sc_bytes([
    0xEC, 0xD3, 0xF5, 0x5C, 0x1A, 0x63, 0x12, 0x58,
    0xD6, 0x9C, 0xF7, 0xA2, 0xDE, 0xF9, 0xDE, 0x14,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10
])

sc_bytes_ZERO = sc_bytes([ 0x00 ] * 32)

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
