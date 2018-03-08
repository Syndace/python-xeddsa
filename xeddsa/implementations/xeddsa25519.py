import copy
import hashlib

from ..xeddsa import XEdDSA, bytesToString, toBytes

import ref10

from nacl.exceptions import BadSignatureError
from nacl.public import PrivateKey as Curve25519DecryptionKey
from nacl.signing import VerifyKey as Ed25519VerificationKey

class Ed25519Math(object):
    p = pow(2, 255) - 19
    q = pow(2, 252) + 27742317777372353535851937790883648493
    b = 256

    @staticmethod
    def bytes_to_int(bytes):
        value = 0

        for i in range(len(bytes)):
            value |= bytes[i] << (i * 8)

        return value

    @staticmethod
    def int_to_bytes(value):
        result = []

        for i in range(32):
            result.append(value & 0xFF)
            value >>= 8

        return result

    @staticmethod
    def cmov(a_bytes, b_bytes, condition):
        # Create an 8 bit mask of either all zeros or all ones
        condition = (condition << 0 | condition << 1 |
                     condition << 2 | condition << 3 |
                     condition << 4 | condition << 5 |
                     condition << 6 | condition << 7 )

        tmp = [ 0x00 ] * 32

        # Mix (xor) together a and b
        for i in range(32):
            tmp[i] = a_bytes[i] ^ b_bytes[i]

        # Either keep the mixed values as they are or reset them to zeros
        for i in range(32):
            tmp[i] &= condition

        # Build the resulting values:
        # y contains either a ^ b bytes or zeros, x contains bytes of a.
        # If y contains zeros, the result will be a.
        # Otherwise, a ^ a ^ b will get calculated which results in b.
        for i in range(32):
            a_bytes[i] ^= tmp[i]
    
    @classmethod
    def inv(cls, bytes):
        value = cls.bytes_to_int(bytes)
        result = pow(value, cls.p - 2, cls.p)
        return cls.int_to_bytes(result)

    q_minus_one = [ 0xec, 0xd3, 0xf5, 0x5c, 0x1a, 0x63, 0x12, 0x58, 0xd6, 0x9c, 0xf7, 0xa2, 0xde, 0xf9, 0xde, 0x14, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x10 ]

    @classmethod
    def neg(cls, bytes):
        value = cls.bytes_to_int(bytes)
        minus_one = cls.bytes_to_int(cls.q_minus_one)
        result = (value * minus_one) % cls.q
        return cls.int_to_bytes(result)

    @classmethod
    def mod(cls, bytes, modulus):
        value = cls.bytes_to_int(bytes)
        result = value % modulus
        return cls.int_to_bytes(result)

    @classmethod
    def sub(cls, minuend_bytes, subtrahend):
        minuend = cls.bytes_to_int(minuend_bytes)
        result = minuend - subtrahend
        return cls.int_to_bytes(result)

    @classmethod
    def add(cls, addend_a_bytes, addend_b):
        addend_a = cls.bytes_to_int(addend_a_bytes)
        result = addend_a + addend_b
        return cls.int_to_bytes(result)

    @classmethod
    def mul(cls, multiplicand_bytes, multiplier_bytes, modulus):
        multiplicand = cls.bytes_to_int(multiplicand_bytes)
        multiplier   = cls.bytes_to_int(multiplier_bytes)

        result = (multiplicand * multiplier) % modulus

        return cls.int_to_bytes(result)

    @classmethod
    def muladd(cls, multiplicand_bytes, multiplier_bytes, addend_bytes, modulus):
        multiplicand = cls.bytes_to_int(multiplicand_bytes)
        multiplier   = cls.bytes_to_int(multiplier_bytes)
        addend       = cls.bytes_to_int(addend_bytes)

        result = (multiplicand * multiplier + addend) % modulus

        return cls.int_to_bytes(result)

class XEdDSA25519(XEdDSA):
    @classmethod
    def _restoreEncryptionKey(cls, decryption_key):
        return toBytes(bytes(Curve25519DecryptionKey(bytesToString(decryption_key)).public_key))

    @classmethod
    def _sign(cls, message, nonce, verification_key, signing_key):
        # Aliases for consistency with the specification
        M = message
        Z = nonce

        # A, a = calculate_key_pair(k)
        A = verification_key
        a = signing_key

        # r = hash_1(a || M || Z) (mod q)
        r = cls.__hash(cls.__concat(a, M, Z), 1) % Ed25519Math.q
        r = Ed25519Math.int_to_bytes(r)

        # R = rB
        R = ref10.ge_p3_tobytes(ref10.ge_scalarmult_base(r))

        # h = hash(R || A || M) (mod q)
        h = cls.__hash(cls.__concat(R, A, M)) % Ed25519Math.q
        h = Ed25519Math.int_to_bytes(h)

        # s = r + ha (mod q)
        s = Ed25519Math.muladd(h, a, r, Ed25519Math.q)

        return cls.__concat(R, s)

    @classmethod
    def _verify(cls, message, signature, verification_key):
        verification_key = bytesToString(verification_key)
        signature        = bytesToString(signature)
        message          = bytesToString(message)

        try:
            return Ed25519VerificationKey(verification_key).verify(message, signature) == message
        except BadSignatureError:
            return False

    @classmethod
    def _mont_priv_to_ed_pair(cls, mont_priv):
        # Prepare the buffer of the resuling twisted Edwards private key
        ed_priv = copy.deepcopy(mont_priv)

        # Get the twisted edwards public key, including the sign bit
        ed_pub = ref10.ge_p3_tobytes(ref10.ge_scalarmult_base(ed_priv))

        # Save the sign bit for later
        sign_bit = (ed_pub[31] & 0x80) >> 7

        # Force the sign bit to zero
        ed_pub[31] &= 0x7F

        # Prepare the negated private key
        ed_priv_neg = Ed25519Math.neg(ed_priv)

        # Get the correct private key based on the sign stored above
        Ed25519Math.cmov(ed_priv, ed_priv_neg, sign_bit)

        return ed_pub, ed_priv

    @classmethod
    def _mont_pub_to_ed_pub(cls, mont_pub):
        # Mask off excess bits from the Montgomery public key
        mont_pub_masked = Ed25519Math.mod(mont_pub, pow(2, 255))

        # Convert the Montgomery public key to a twisted Edwards public key by calculating
        # y = (u - 1) * inv(u + 1) (mod p)
        mont_pub_minus_one    = Ed25519Math.sub(mont_pub_masked, 1)
        mont_pub_plus_one     = Ed25519Math.add(mont_pub_masked, 1)
        mont_pub_plus_one_inv = Ed25519Math.inv(mont_pub_plus_one)

        ed_pub = Ed25519Math.mul(mont_pub_minus_one, mont_pub_plus_one_inv, Ed25519Math.p)

        # Force the sign bit to zero
        ed_pub[31] &= 0x7F

        return ed_pub

    @staticmethod
    def __concat(*bytes):
        return reduce(lambda x, y: x + y, bytes)

    @classmethod
    def __hash(cls, bytes, index = None):
        def _hash(data):
            bytestring = bytesToString(data)
            hash_digest = hashlib.sha512(bytestring).digest()
            return Ed25519Math.bytes_to_int(toBytes(hash_digest))

        if index:
            padding_int = pow(2, Ed25519Math.b) - 1 - index
            padding = Ed25519Math.int_to_bytes(padding_int)
            data = cls.__concat(padding, bytes)
            return _hash(data)
        else:
            return _hash(bytes)
