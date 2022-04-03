from typing import Optional

class cdata:
    def __bytes__(self) -> bytes: ...

class lib:
    @staticmethod
    def ed25519_priv_sign(sig: cdata, priv: cdata, msg: cdata, msg_size: int, nonce: cdata) -> None: ...

    @staticmethod
    def ed25519_seed_sign(sig: cdata, seed: cdata, msg: cdata, msg_size: int) -> None: ...

    @staticmethod
    def ed25519_verify(sig: cdata, ed25519_pub: cdata, msg: cdata, msg_size: int) -> int: ...

    @staticmethod
    def curve25519_pub_to_ed25519_pub(ed25519_pub: cdata, curve25519_pub: cdata, set_sign_bit: bool) -> None: ...

    @staticmethod
    def ed25519_pub_to_curve25519_pub(curve25519_pub: cdata, ed25519_pub: cdata) -> int: ...

    @staticmethod
    def priv_to_curve25519_pub(curve25519_pub: cdata, priv: cdata) -> None: ...

    @staticmethod
    def priv_to_ed25519_pub(ed25519_pub: cdata, priv: cdata) -> None: ...

    @staticmethod
    def seed_to_ed25519_pub(ed25519_pub: cdata, seed: cdata) -> None: ...

    @staticmethod
    def priv_force_sign(priv_out: cdata, priv_in: cdata, set_sign_bit: bool) -> None: ...

    @staticmethod
    def seed_to_priv(priv: cdata, seed: cdata) -> None: ...

    @staticmethod
    def x25519(shared_secret: cdata, priv: cdata, curve25519_pub: cdata) -> int: ...

    @staticmethod
    def xeddsa_init() -> int: ...

    XEDDSA_VERSION_MAJOR: int
    XEDDSA_VERSION_MINOR: int
    XEDDSA_VERSION_REVISION: int

class ffi:
    @staticmethod
    def new(type_definition: str, data: Optional[bytes] = None) -> cdata: ...
