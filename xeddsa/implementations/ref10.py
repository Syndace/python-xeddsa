# Pylint can't statically verify interaction with the C extension.
# Dynamic introspection of living objects during run-time is not an option either.
# pylint: disable=c-extension-no-member

from typing import ClassVar, TypeVar, Type

import _crypto_sign

class Failed(Exception):
    pass

T = TypeVar("T", bound="FFIType")

class FFIType:
    FFI_TYPE: ClassVar[str] = NotImplemented

    def __init__(self, data):
        self.__data = data

    def get(self):
        return self.__data

    def __bytes__(self) -> bytes:
        return bytes(self.__data)

    @classmethod
    def empty(cls: Type[T]) -> T:
        if cls.FFI_TYPE == NotImplemented:
            raise NotImplementedError("You can't use FFIType directly, but have to subclass it!")

        return cls(_crypto_sign.ffi.new(cls.FFI_TYPE))

    @classmethod
    def wrap(cls: Type[T], data: bytes) -> T:
        return cls(_crypto_sign.ffi.new(cls.FFI_TYPE, data))

###############################################################################
# fe.h                                                                        #
###############################################################################

class FieldElementBytes(FFIType):
    FFI_TYPE: ClassVar[str] = "unsigned char[32]"

class FieldElement(FFIType):
    FFI_TYPE: ClassVar[str] = "int32_t[10]"

def fe_frombytes(fe_bytes: FieldElementBytes) -> FieldElement:
    result = FieldElement.empty()

    _crypto_sign.lib.crypto_sign_ed25519_ref10_fe_frombytes(
        result.get(),
        fe_bytes.get()
    )

    return result

def fe_tobytes(fe: FieldElement) -> FieldElementBytes:
    result = FieldElementBytes.empty()

    _crypto_sign.lib.crypto_sign_ed25519_ref10_fe_tobytes(
        result.get(),
        fe.get()
    )

    return result

def fe_1() -> FieldElement:
    result = FieldElement.empty()

    _crypto_sign.lib.crypto_sign_ed25519_ref10_fe_1(
        result.get()
    )

    return result

def fe_add(addend_a: FieldElement, addend_b: FieldElement) -> FieldElement:
    result = FieldElement.empty()

    _crypto_sign.lib.crypto_sign_ed25519_ref10_fe_add(
        result.get(),
        addend_a.get(),
        addend_b.get()
    )

    return result

def fe_sub(minuend: FieldElement, subtrahend: FieldElement) -> FieldElement:
    result = FieldElement.empty()

    _crypto_sign.lib.crypto_sign_ed25519_ref10_fe_sub(
        result.get(),
        minuend.get(),
        subtrahend.get()
    )

    return result

def fe_mul(multiplicand: FieldElement, multiplier: FieldElement) -> FieldElement:
    result = FieldElement.empty()

    _crypto_sign.lib.crypto_sign_ed25519_ref10_fe_mul(
        result.get(),
        multiplicand.get(),
        multiplier.get()
    )

    return result

def fe_invert(fe: FieldElement) -> FieldElement:
    result = FieldElement.empty()

    _crypto_sign.lib.crypto_sign_ed25519_ref10_fe_invert(
        result.get(),
        fe.get()
    )

    return result

###############################################################################
# ge.h                                                                        #
###############################################################################
class GroupElementP2(FFIType):
    FFI_TYPE: ClassVar[str] = "ge_p2 *"

class GroupElementP2Bytes(FFIType):
    FFI_TYPE: ClassVar[str] = "unsigned char[32]"

def ge_tobytes(ge: GroupElementP2) -> GroupElementP2Bytes:
    result = GroupElementP2Bytes.empty()

    _crypto_sign.lib.crypto_sign_ed25519_ref10_ge_tobytes(
        result.get(),
        ge.get()
    )

    return result

class GroupElementP3(FFIType):
    FFI_TYPE: ClassVar[str] = "ge_p3 *"

class GroupElementP3Bytes(FFIType):
    FFI_TYPE: ClassVar[str] = "unsigned char[32]"

def ge_p3_tobytes(ge: GroupElementP3) -> GroupElementP3Bytes:
    result = GroupElementP3Bytes.empty()

    _crypto_sign.lib.crypto_sign_ed25519_ref10_ge_p3_tobytes(
        result.get(),
        ge.get()
    )

    return result

def ge_frombytes_negate_vartime(ge_bytes: GroupElementP3Bytes) -> GroupElementP3:
    result = GroupElementP3.empty()

    success = _crypto_sign.lib.crypto_sign_ed25519_ref10_ge_frombytes_negate_vartime(
        result.get(),
        ge_bytes.get()
    )

    if success != 0:
        raise Failed()

    return result

class ScalarBytes(FFIType):
    FFI_TYPE: ClassVar[str] = "unsigned char[32]"

def ge_scalarmult_base(sc: ScalarBytes) -> GroupElementP3:
    result = GroupElementP3.empty()

    _crypto_sign.lib.crypto_sign_ed25519_ref10_ge_scalarmult_base(
        result.get(),
        sc.get()
    )

    return result

def ge_double_scalarmult_vartime(sc_a: ScalarBytes, ge: GroupElementP3, sc_b: ScalarBytes) -> GroupElementP2:
    result = GroupElementP2.empty()

    _crypto_sign.lib.crypto_sign_ed25519_ref10_ge_double_scalarmult_vartime(
        result.get(),
        sc_a.get(),
        ge.get(),
        sc_b.get()
    )

    return result

###############################################################################
# sc.h                                                                        #
###############################################################################
class ScalarReduceBytes(FFIType):
    FFI_TYPE: ClassVar[str] = "unsigned char[64]"

    def to_scalar(self) -> ScalarBytes:
        return ScalarBytes.wrap(bytes(self)[:32])

def sc_reduce(sc: ScalarReduceBytes) -> ScalarBytes:
    _crypto_sign.lib.crypto_sign_ed25519_ref10_sc_reduce(
        sc.get()
    )

    return sc.to_scalar()

def sc_muladd(multiplicand: ScalarBytes, multiplier: ScalarBytes, addend: ScalarBytes) -> ScalarBytes:
    result = ScalarBytes.empty()

    _crypto_sign.lib.crypto_sign_ed25519_ref10_sc_muladd(
        result.get(),
        multiplicand.get(),
        multiplier.get(),
        addend.get()
    )

    return result

###############################################################################
# XEdDSA additions                                                            #
###############################################################################
BASE_POINT_ORDER_MINUS_ONE = ScalarBytes.wrap(bytes([
    0xEC, 0xD3, 0xF5, 0x5C, 0x1A, 0x63, 0x12, 0x58,
    0xD6, 0x9C, 0xF7, 0xA2, 0xDE, 0xF9, 0xDE, 0x14,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10
]))

ZERO = ScalarBytes.wrap(bytes([ 0x00 ] * 32))

def sc_neg(sc: ScalarBytes) -> ScalarBytes:
    return sc_muladd(BASE_POINT_ORDER_MINUS_ONE, sc, ZERO)

def sc_cmov(sc_a: ScalarBytes, sc_b: ScalarBytes, condition: bool) -> ScalarBytes:
    condition_bit = int(condition)

    # Create an eight bit mask for the condition, either all ones or all zeros
    condition_mask = ( condition_bit << 0 |
                       condition_bit << 1 |
                       condition_bit << 2 |
                       condition_bit << 3 |
                       condition_bit << 4 |
                       condition_bit << 5 |
                       condition_bit << 6 |
                       condition_bit << 7 )

    sc_bytes_a = bytes(sc_a)
    sc_bytes_b = bytes(sc_b)

    result_mut = bytearray(sc_bytes_a)

    for i in range(32):
        # Mix together the two scalars a and b by xor'ing them
        # tmp = a ^ b
        tmp = sc_bytes_a[i] ^ sc_bytes_b[i]

        # Now, apply the condition mask to the temporary result, which creates either of:
        # - tmp = (a ^ b) & 0xFF = a ^ b, if the condition is true
        # - tmp = (a ^ b) & 0x00 = 0    , if the condition is false
        tmp &= condition_mask

        # Finally, xor the temporary result with the bytes of a.
        # This results in either of the following based on the condition:
        # - a ^ tmp = a ^ (a ^ b) = b, if the condition is true
        # - a ^ tmp = a ^ (0    ) = a, if the condition is false
        result_mut[i] ^= tmp

    return ScalarBytes.wrap(bytes(result_mut))
