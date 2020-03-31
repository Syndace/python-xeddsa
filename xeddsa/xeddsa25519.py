from typing import ClassVar

import libnacl

from .bindings import (
    curve25519_sign, curve25519_pub_to_ed25519_pub,
    Curve25519Priv, Curve25519Pub, Ed25519Pub, Ed25519Signature, Nonce
)

from .xeddsa import XEdDSA

class XEdDSA25519(XEdDSA):
    """
    An implementation of XEdDSA for Montgomery Curve25519 and twisted Edwards Ed25519 keys.
    """

    MONT_PRIV_KEY_SIZE : ClassVar[int] = 32
    MONT_PUB_KEY_SIZE  : ClassVar[int] = 32
    ED_PUB_KEY_SIZE    : ClassVar[int] = 32
    SIGNATURE_SIZE     : ClassVar[int] = 64

    @staticmethod
    def _generate_mont_priv() -> Curve25519Priv:
        return libnacl.crypto_box_keypair()[1]

    @staticmethod
    def _mont_pub_from_mont_priv(mont_priv: Curve25519Priv) -> Curve25519Pub:
        return libnacl.crypto_scalarmult_base(mont_priv)

    @staticmethod
    def _mont_pub_to_ed_pub(mont_pub: Curve25519Pub) -> Ed25519Pub:
        return curve25519_pub_to_ed25519_pub(mont_pub)

    @staticmethod
    def _sign(mont_priv: Curve25519Priv, msg: bytes, nonce: Nonce) -> Ed25519Signature:
        return curve25519_sign(mont_priv, msg, nonce)

    @staticmethod
    def _verify(ed_pub: Ed25519Pub, msg: bytes, sig: Ed25519Signature) -> bool:
        try:
            return libnacl.crypto_sign_verify_detached(sig, msg, ed_pub) == msg
        except ValueError:
            return False
