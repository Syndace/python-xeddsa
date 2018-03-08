from ctypes import *

ref10 = cdll.LoadLibrary("libref10.so")

###############################################################################
# fe.h                                                                        #
###############################################################################
fe = c_int32 * 10
fe_bytes = c_uint8 * 32

###############################################################################
# ge.h                                                                        #
###############################################################################
class ge_p2(Structure):
    _fields_ = [("X", fe),
                ("Y", fe),
                ("Z", fe)]

ge_p2_bytes = c_uint8 * 32

class ge_p3(Structure):
    _fields_ = [("X", fe),
                ("Y", fe),
                ("Z", fe),
                ("T", fe)]

ge_p3_bytes = c_uint8 * 32

class ge_p1p1(Structure):
    _fields_ = [("X", fe),
                ("Y", fe),
                ("Z", fe),
                ("T", fe)]

class ge_precomp(Structure):
    _fields_ = [("yplusx",  fe),
                ("yminusx", fe),
                ("xy2d",    fe)]

class ge_cached(Structure):
    _fields_ = [("YplusX",  fe),
                ("YminusX", fe),
                ("Z",       fe),
                ("T2d",     fe)]

def ge_tobytes(ge_p2_POINT):
    result = ge_p2_bytes()
    ref10.crypto_sign_ed25519_ref10_ge_tobytes(result, byref(ge_p2_POINT))
    return list(result)

def ge_p3_tobytes(ge_p3_POINT):
    result = ge_p3_bytes()
    ref10.crypto_sign_ed25519_ref10_ge_p3_tobytes(result, byref(ge_p3_POINT))
    return list(result)

def ge_frombytes_negate_vartime(ge_p3_bytes_BYTES):
    result = ge_p3()
    ref10.crypto_sign_ed25519_ref10_ge_frombytes_negate_vartime(byref(result), ge_p3_bytes_BYTES)
    return result

scalar_bytes = c_uint8 * 32

def ge_scalarmult_base(scalar_bytes_SCALAR):
    if not isinstance(scalar_bytes_SCALAR, scalar_bytes):
        scalar_bytes_SCALAR = scalar_bytes(*scalar_bytes_SCALAR)

    result = ge_p3()
    ref10.crypto_sign_ed25519_ref10_ge_scalarmult_base(byref(result), scalar_bytes_SCALAR)
    return result
