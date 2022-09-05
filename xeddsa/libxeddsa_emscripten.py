# pylint: skip-file

from browser import window  # type: ignore[import]
import re
from typing import Any, Optional, cast


__all__ = [
    "cdata",
    "lib",
    "ffi"
]


class cdata:
    def __init__(self, array: Any) -> None:
        self.__array = array

    @property
    def array(self) -> Any:
        return self.__array

    def __bytes__(self) -> bytes:
        return bytes(window.Array["from"](self.__array))


class lib:
    @staticmethod
    def ed25519_priv_sign(sig: cdata, priv: cdata, msg: cdata, msg_size: int, nonce: cdata) -> None:
        sig_ptr = window.Module._malloc(sig.array.length)

        window.ed25519_priv_sign(sig_ptr, priv.array, msg.array, msg_size, nonce.array)

        sig.array.set(window.HEAPU8.subarray(sig_ptr, sig_ptr + sig.array.length))
        window.Module._free(sig_ptr)

    @staticmethod
    def ed25519_seed_sign(sig: cdata, seed: cdata, msg: cdata, msg_size: int) -> None:
        sig_ptr = window.Module._malloc(sig.array.length)

        window.ed25519_seed_sign(sig_ptr, seed.array, msg.array, msg_size)

        sig.array.set(window.HEAPU8.subarray(sig_ptr, sig_ptr + sig.array.length))
        window.Module._free(sig_ptr)

    @staticmethod
    def ed25519_verify(sig: cdata, ed25519_pub: cdata, msg: cdata, msg_size: int) -> int:
        return cast(int, window.ed25519_verify(sig.array, ed25519_pub.array, msg.array, msg_size))

    @staticmethod
    def curve25519_pub_to_ed25519_pub(ed25519_pub: cdata, curve25519_pub: cdata, set_sign_bit: bool) -> None:
        ed25519_pub_ptr = window.Module._malloc(ed25519_pub.array.length)

        window.curve25519_pub_to_ed25519_pub(ed25519_pub_ptr, curve25519_pub.array, set_sign_bit)

        ed25519_pub.array.set(window.HEAPU8.subarray(
            ed25519_pub_ptr,
            ed25519_pub_ptr + ed25519_pub.array.length
        ))
        window.Module._free(ed25519_pub_ptr)

    @staticmethod
    def ed25519_pub_to_curve25519_pub(curve25519_pub: cdata, ed25519_pub: cdata) -> int:
        curve25519_pub_ptr = window.Module._malloc(curve25519_pub.array.length)

        result = cast(int, window.ed25519_pub_to_curve25519_pub(curve25519_pub_ptr, ed25519_pub.array))

        curve25519_pub.array.set(window.HEAPU8.subarray(
            curve25519_pub_ptr,
            curve25519_pub_ptr + curve25519_pub.array.length
        ))
        window.Module._free(curve25519_pub_ptr)

        return result

    @staticmethod
    def priv_to_curve25519_pub(curve25519_pub: cdata, priv: cdata) -> None:
        curve25519_pub_ptr = window.Module._malloc(curve25519_pub.array.length)

        window.priv_to_curve25519_pub(curve25519_pub_ptr, priv.array)

        curve25519_pub.array.set(window.HEAPU8.subarray(
            curve25519_pub_ptr,
            curve25519_pub_ptr + curve25519_pub.array.length
        ))
        window.Module._free(curve25519_pub_ptr)

    @staticmethod
    def priv_to_ed25519_pub(ed25519_pub: cdata, priv: cdata) -> None:
        ed25519_pub_ptr = window.Module._malloc(ed25519_pub.array.length)

        window.priv_to_ed25519_pub(ed25519_pub_ptr, priv.array)

        ed25519_pub.array.set(window.HEAPU8.subarray(
            ed25519_pub_ptr,
            ed25519_pub_ptr + ed25519_pub.array.length
        ))
        window.Module._free(ed25519_pub_ptr)

    @staticmethod
    def seed_to_ed25519_pub(ed25519_pub: cdata, seed: cdata) -> None:
        ed25519_pub_ptr = window.Module._malloc(ed25519_pub.array.length)

        window.seed_to_ed25519_pub(ed25519_pub_ptr, seed.array)

        ed25519_pub.array.set(window.HEAPU8.subarray(
            ed25519_pub_ptr,
            ed25519_pub_ptr + ed25519_pub.array.length
        ))
        window.Module._free(ed25519_pub_ptr)

    @staticmethod
    def priv_force_sign(priv_out: cdata, priv_in: cdata, set_sign_bit: bool) -> None:
        priv_out_ptr = window.Module._malloc(priv_out.array.length)

        window.priv_force_sign(priv_out_ptr, priv_in.array, set_sign_bit)

        priv_out.array.set(window.HEAPU8.subarray(
            priv_out_ptr,
            priv_out_ptr + priv_out.array.length
        ))
        window.Module._free(priv_out_ptr)

    @staticmethod
    def seed_to_priv(priv: cdata, seed: cdata) -> None:
        priv_ptr = window.Module._malloc(priv.array.length)

        window.seed_to_priv(priv_ptr, seed.array)

        priv.array.set(window.HEAPU8.subarray(priv_ptr, priv_ptr + priv.array.length))
        window.Module._free(priv_ptr)

    @staticmethod
    def x25519(shared_secret: cdata, priv: cdata, curve25519_pub: cdata) -> int:
        shared_secret_ptr = window.Module._malloc(shared_secret.array.length)

        result = cast(int, window.x25519(shared_secret_ptr, priv.array, curve25519_pub.array))

        shared_secret.array.set(window.HEAPU8.subarray(
            shared_secret_ptr,
            shared_secret_ptr + shared_secret.array.length
        ))
        window.Module._free(shared_secret_ptr)

        return result

    @staticmethod
    def xeddsa_init() -> int:
        return cast(int, window.xeddsa_init())

    XEDDSA_VERSION_MAJOR: int = window.XEDDSA_VERSION_MAJOR
    XEDDSA_VERSION_MINOR: int = window.XEDDSA_VERSION_MINOR
    XEDDSA_VERSION_REVISION: int = window.XEDDSA_VERSION_REVISION


class ffi:
    @staticmethod
    def new(type_definition: str, data: Optional[bytes] = None) -> cdata:
        match = re.match(r"uint8_t\[(\d+)?\]", type_definition)
        if match is None:
            raise ValueError("Only uint8_t arrays are supported for now.")

        array_size = match.group(1)
        if array_size is None and data is None:
            raise ValueError("Data must be supplied if an array of unknown size is requested.")

        return cdata(
            window.Uint8Array.new(array_size)
            if data is None
            else window.Uint8Array["from"](list(data))
        )
