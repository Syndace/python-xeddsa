from typing import ClassVar, Tuple

import libnacl

from ..xeddsa import XEdDSA, MontPriv, MontPub, EdPriv, EdPub, Signature, Nonce

from .ref10 import (
    FieldElementBytes,
    fe_frombytes,
    fe_tobytes,
    fe_1,
    fe_add,
    fe_sub,
    fe_mul,
    fe_invert,

    ge_p3_tobytes,
    ScalarBytes,
    ge_scalarmult_base,

    ScalarReduceBytes,
    sc_reduce,
    sc_muladd,

    sc_neg,
    sc_cmov
)

class XEdDSA25519(XEdDSA):
    """
    An implementation of XEdDSA for Montgomery Curve25519 and Twisted Edwards Ed25519 keys.
    """

    MONT_PRIV_KEY_SIZE : ClassVar[int] = 32
    MONT_PUB_KEY_SIZE  : ClassVar[int] = 32
    ED_PRIV_KEY_SIZE   : ClassVar[int] = 32
    ED_PUB_KEY_SIZE    : ClassVar[int] = 32
    SIGNATURE_SIZE     : ClassVar[int] = 64

    @staticmethod
    def _generate_mont_priv() -> MontPriv:
        result_mut = bytearray(libnacl.crypto_box_keypair()[1])

        result_mut[0]  &= 248
        result_mut[31] &= 127
        result_mut[31] |=  64

        return bytes(result_mut)

    @staticmethod
    def _mont_pub_from_mont_priv(mont_priv: MontPriv) -> MontPub:
        return libnacl.crypto_scalarmult_base(mont_priv)

    @staticmethod
    def _mont_priv_to_ed_pair(mont_priv: MontPriv) -> Tuple[EdPriv, EdPub]:
        ed_priv = ScalarBytes.wrap(mont_priv)

        # Get the Twisted Edwards public key, including the sign bit
        ed_pub = bytes(ge_p3_tobytes(ge_scalarmult_base(ed_priv)))

        # Save the sign bit for later
        sign_bit = bool((ed_pub[31] >> 7) & 1)

        # Force the sign bit to zero
        ed_pub_mut = bytearray(ed_pub)
        ed_pub_mut[31] &= 0x7F
        ed_pub = bytes(ed_pub_mut)

        # Prepare the negated private key
        ed_priv_neg = sc_neg(ed_priv)

        # Get the correct private key based on the sign stored above
        ed_priv = sc_cmov(ed_priv, ed_priv_neg, sign_bit)

        return bytes(ed_priv), bytes(ed_pub)

    @staticmethod
    def _mont_pub_to_ed_pub(mont_pub: MontPub) -> EdPub:
        # Read the public key as a field element
        mont_pub_fe = fe_frombytes(FieldElementBytes.wrap(mont_pub))

        # Convert the Montgomery public key to a twisted Edwards public key
        one = fe_1()

        # Calculate the parameters (u - 1) and (u + 1)
        mont_pub_minus_one = fe_sub(mont_pub_fe, one)
        mont_pub_plus_one  = fe_add(mont_pub_fe, one)

        # Prepare inv(u + 1)
        mont_pub_plus_one = fe_invert(mont_pub_plus_one)

        # Calculate y = (u - 1) * inv(u + 1) (mod p)
        ed_pub = fe_mul(mont_pub_minus_one, mont_pub_plus_one)

        return bytes(fe_tobytes(ed_pub))

    @staticmethod
    def _sign(data: bytes, nonce: Nonce, ed_priv: EdPriv, ed_pub: EdPub) -> Signature:
        # pylint: disable=invalid-name

        # Aliases for consistency with the specification
        M = data
        Z = nonce

        # A, a = calculate_key_pair(k)
        A = ed_pub
        a = ed_priv

        # r = hash_1(a || M || Z) (mod q)

        # If the hash has an index as above, that means, we are supposed to calculate:
        #     hash(2 ^ b - 1 - i || X)
        #
        # If b = 256 (which is the case for 25519 XEdDSA), then 2 ^ b - 1 = [ 0xFF ] * 32
        # Now, subtracting i from the result can be done by subtracting i from the first
        # byte (assuming i <= 0xFF).
        padding_mut = bytearray(b"\xFF" * 32)
        padding_mut[0] -= 1
        padding = bytes(padding_mut)
        r = libnacl.crypto_hash_sha512(padding + a + M + Z)
        r_sc = sc_reduce(ScalarReduceBytes.wrap(r))

        # R = rB
        R = bytes(ge_p3_tobytes(ge_scalarmult_base(r_sc)))

        # h = hash(R || A || M) (mod q)
        h = libnacl.crypto_hash_sha512(R + A + M)
        h_sc = sc_reduce(ScalarReduceBytes.wrap(h))

        # s = r + ha (mod q)
        s = bytes(sc_muladd(h_sc, ScalarBytes.wrap(a), r_sc))

        return R + s

    @staticmethod
    def _verify(data: bytes, signature: Signature, ed_pub: EdPub) -> bool:
        # Get the sign bit from the signature.
        # This part of the signature is usually unused, but the XEdDSA implementation of libsignal uses the
        # bit to store information about the sign of the public key. Before verification, this sign bit has to
        # be removed from the signature and restored on the public key, which should have a sign bit of 0 at
        # this point.
        sign_bit = (signature[63] >> 7) & 1

        # Set the sign bit to zero in the signature.
        signature_mut = bytearray(signature)
        signature_mut[63] &= 0x7F
        signature = bytes(signature_mut)

        # Restore the sign bit on the verification key, which should have 0 as its current sign bit.
        ed_pub_mut = bytearray(ed_pub)
        ed_pub_mut[31] |= sign_bit << 7
        ed_pub = bytes(ed_pub_mut)

        # From this point on, the signature should be a valid EdDSA signature and thus be verifyable by
        # libsodium or other libraries that implement Ed25519 signatures.
        try:
            return libnacl.crypto_sign_verify_detached(signature, data, ed_pub) == data
        except ValueError:
            return False
