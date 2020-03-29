from typing import Optional

class cdata:
    def __bytes__(self) -> bytes: ...

class lib:
    @staticmethod
    def xeddsa_init() -> int: ...

    @staticmethod
    def curve25519_sign(sig: cdata, curve25519_priv: cdata, msg: cdata, msg_size: int, nonce: cdata): ...

    @staticmethod
    def curve25519_pub_to_ed25519_pub(ed25519_pub: cdata, curve25519_pub: cdata): ...

class ffi:
    @staticmethod
    def new(type_definition: str, data: Optional[bytes] = None) -> cdata: ...
