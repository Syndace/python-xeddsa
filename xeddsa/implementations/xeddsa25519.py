import copy
import hashlib

# I can't believe they moved reduce from the global space :(
from functools import reduce

from ..xeddsa import XEdDSA, bytesToString, toBytes

from .ref10 import *

from nacl.exceptions import BadSignatureError
from nacl.public import PrivateKey as Curve25519DecryptionKey
from nacl.signing import VerifyKey as Ed25519VerificationKey

def sc_fromint(value):
    result = []

    for i in range(32):
        result.append(value & 0xFF)
        value >>= 8

    return result

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
        r = cls.__hash(cls.__concat(a, M, Z), 1)
        r = sc_reduce(r)

        # R = rB
        R = list(ge_p3_tobytes(ge_scalarmult_base(r)))

        # h = hash(R || A || M) (mod q)
        h = cls.__hash(cls.__concat(R, A, M))
        h = sc_reduce(h)

        # s = r + ha (mod q)
        s = list(sc_muladd(h, a, r))

        return bytesToString(cls.__concat(R, s))

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
        # Prepare a buffer for the twisted Edwards private key
        ed_priv = copy.deepcopy(mont_priv)

        # Get the twisted edwards public key, including the sign bit
        ed_pub = ge_p3_tobytes(ge_scalarmult_base(mont_priv))

        # Save the sign bit for later
        sign_bit = (ed_pub[31] >> 7) & 1

        # Force the sign bit to zero
        ed_pub[31] &= 0x7F

        # Prepare the negated private key
        ed_priv_neg = sc_neg(ed_priv)

        # Get the correct private key based on the sign stored above
        sc_cmov(ed_priv, ed_priv_neg, sign_bit)

        return list(ed_pub), ed_priv

    @classmethod
    def _mont_pub_to_ed_pub(cls, mont_pub):
        # Read the public key as a field element
        mont_pub = fe_frombytes(mont_pub)

        # Convert the Montgomery public key to a twisted Edwards public key
        fe_ONE = fe_1()

        # Calculate the parameters (u - 1) and (u + 1)
        mont_pub_minus_one = fe_sub(mont_pub, fe_ONE)
        mont_pub_plus_one  = fe_add(mont_pub, fe_ONE)

        # Prepare inv(u + 1)
        mont_pub_plus_one_inv = fe_invert(mont_pub_plus_one)

        # Calculate y = (u - 1) * inv(u + 1) (mod p)
        ed_pub = fe_mul(mont_pub_minus_one, mont_pub_plus_one_inv)
        ed_pub = fe_tobytes(ed_pub)

        return list(ed_pub)

    @staticmethod
    def __concat(*bytes):
        return reduce(lambda x, y: x + y, bytes)

    @classmethod
    def __hash(cls, bytes, index = None):
        def _hash(data):
            bytestring = bytesToString(data)
            hash_digest = hashlib.sha512(bytestring).digest()
            return toBytes(hash_digest)

        if index:
            padding_int = pow(2, 256) - 1 - index
            padding = sc_fromint(padding_int)
            data = cls.__concat(padding, bytes)
            return _hash(data)
        else:
            return _hash(bytes)
