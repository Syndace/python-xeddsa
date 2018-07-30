from __future__ import absolute_import

import copy
import hashlib
import os

from ..xeddsa import XEdDSA, bytesToString, toBytes

from .ref10 import *

from nacl.exceptions import BadSignatureError
from nacl.public import PrivateKey as Curve25519DecryptionKey
from nacl.signing import VerifyKey as Ed25519VerificationKey

class XEdDSA25519(XEdDSA):
    @staticmethod
    def generateDecryptionKey():
        priv = toBytes(os.urandom(32))

        # The following step is referred to as "clamping".
        # The following links to a mailing list discussion about what clamping does:
        # https://moderncrypto.org/mail-archive/curves/2017/000858.html

        # I am not sure why, but without clamping the private key XEdDSA does not work.
        # Maybe the ref10 implementation expects all scalars to be clamped.
        priv[0]  &= 248
        priv[31] &=  63
        priv[31] |=  64

        return bytesToString(priv)

    @staticmethod
    def restoreEncryptionKey(decryption_key):
        return bytes(Curve25519DecryptionKey(bytesToString(decryption_key)).public_key)

    @classmethod
    def _sign(cls, message, nonce, verification_key, signing_key):
        # Aliases for consistency with the specification
        M = message
        Z = nonce

        # A, a = calculate_key_pair(k)
        A = verification_key
        a = signing_key

        # r = hash_1(a || M || Z) (mod q)
        r = cls.__hash(a + M + Z, 1)
        r = sc_reduce(r)

        # R = rB
        R = list(ge_p3_tobytes(ge_scalarmult_base(r)))

        # h = hash(R || A || M) (mod q)
        h = cls.__hash(R + A + M)
        h = sc_reduce(h)

        # s = r + ha (mod q)
        s = list(sc_muladd(h, a, r))

        return toBytes(R + s)

    @classmethod
    def _verify(cls, message, signature, verification_key):
        # Here we use the fact, that
        # "XEd25519 signatures are valid Ed25519 signatures [1] and vice versa, [...]."
        # (https://signal.org/docs/specifications/xeddsa/#curve25519)
        # to reduce the amount of security critical code we have to write ourselves.

        verification_key = bytesToString(verification_key)
        signature        = bytesToString(signature)
        message          = bytesToString(message)

        try:
            return Ed25519VerificationKey(verification_key).verify(message, signature) == message
        except BadSignatureError:
            return False

    @classmethod
    def _mont_priv_to_ed_pair(cls, mont_priv):
        mont_priv = toBytes(mont_priv)

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

        return bytesToString(list(ed_pub)), bytesToString(ed_priv)

    @classmethod
    def _mont_pub_to_ed_pub(cls, mont_pub):
        mont_pub = toBytes(mont_pub)

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

        return bytesToString(list(ed_pub))

    @classmethod
    def __hash(cls, bytes, index = None):
        def _hash(data):
            return toBytes(hashlib.sha512(bytesToString(data)).digest())

        if index:
            # If an index is set, we are supposed to calculate:
            #     hash(2 ^ b - 1 - i || X)
            #
            # If b = 256, then 2 ^ b - 1 = [ 0xFF ] * 32
            # Now, subtracting i from the result can be done like this,
            # assuming i <= 0xFF
            padding = [ 0xFF ] * 32
            padding[0] -= index
            return _hash(padding + bytes)
        else:
            return _hash(bytes)
