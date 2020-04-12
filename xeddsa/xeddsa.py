from abc import ABCMeta, abstractmethod
from typing import Optional

import libnacl

from .bindings import Nonce

MontPriv  = bytes
MontPub   = bytes
EdPub     = bytes
Signature = bytes

class MissingKeyException(Exception):
    pass

class XEdDSA(metaclass=ABCMeta):
    """
    The abstract base class for all XEdDSA implementations.
    """

    @staticmethod
    @abstractmethod
    def _get_mont_priv_key_size() -> int:
        raise NotImplementedError("Create a subclass of XEdDSA and implement `_get_mont_priv_key_size`.")

    @staticmethod
    @abstractmethod
    def _get_mont_pub_key_size() -> int:
        raise NotImplementedError("Create a subclass of XEdDSA and implement `_get_mont_pub_key_size`.")

    @staticmethod
    @abstractmethod
    def _get_ed_pub_key_size() -> int:
        raise NotImplementedError("Create a subclass of XEdDSA and implement `_get_ed_pub_key_size`.")

    @staticmethod
    @abstractmethod
    def _get_signature_size() -> int:
        raise NotImplementedError("Create a subclass of XEdDSA and implement `_get_signature_size`.")

    def __init__(self, mont_priv: Optional[MontPriv] = None, mont_pub: Optional[MontPub] = None):
        """
        Create an XEdDSA object from Montgomery key material, to encrypt AND sign data using just one
        Montgomery key pair.

        Args:
            mont_priv: The Montgomery private key.
            mont_pub: The Montgomery public key.

        If both ``mont_priv`` and ``mont_pub`` are :obj:`None`, a new key pair is generated.
        """

        wanted_mont_priv_key_size = self._get_mont_priv_key_size()
        wanted_mont_pub_key_size  = self._get_mont_pub_key_size()

        if mont_priv is None and mont_pub is None:
            mont_priv = self.generate_mont_priv()

        if mont_priv is not None and len(mont_priv) != wanted_mont_priv_key_size:
            raise ValueError("The Montgomery private key must consist of {} bytes if given.".format(
                wanted_mont_priv_key_size
            ))

        if mont_priv is not None and mont_pub is None:
            mont_pub = self.mont_pub_from_mont_priv(mont_priv)

        if mont_pub is not None and len(mont_pub) != wanted_mont_pub_key_size:
            raise ValueError("The Montgomery public key must consist of {} bytes if given.".format(
                wanted_mont_pub_key_size
            ))

        assert mont_pub is not None # sanity check, to satisfy mypy

        self.__mont_priv: Optional[MontPriv] = mont_priv
        self.__mont_pub: MontPub = mont_pub

    @property
    def mont_priv(self) -> Optional[MontPriv]:
        return self.__mont_priv

    @property
    def mont_pub(self) -> MontPub:
        return self.__mont_pub

    @classmethod
    def generate_mont_priv(cls) -> MontPriv:
        """
        Returns:
            A freshly generated Montgomery private key to be used with XEdDSA.
        """

        return cls._generate_mont_priv()

    @staticmethod
    @abstractmethod
    def _generate_mont_priv() -> MontPriv:
        """
        Returns:
            A freshly generated Montgomery private key to be used with XEdDSA.
        """

        raise NotImplementedError("Create a subclass of XEdDSA and implement `_generate_mont_priv`.")

    @classmethod
    def mont_pub_from_mont_priv(cls, mont_priv: MontPriv) -> MontPub:
        """
        Args:
            mont_priv: The Montgomery private key.

        Returns:
            The Montgomery public key restored from the Montgomery private key.
        """

        wanted_size = cls._get_mont_priv_key_size()
        if len(mont_priv) != wanted_size:
            raise ValueError("The Montgomery private key must consist of {} bytes.".format(wanted_size))

        return cls._mont_pub_from_mont_priv(mont_priv)

    @staticmethod
    @abstractmethod
    def _mont_pub_from_mont_priv(mont_priv: MontPriv) -> MontPub:
        """
        Args:
            mont_priv: The Montgomery private key.

        Returns:
            The Montgomery public key restored from the Montgomery private key.
        """

        raise NotImplementedError("Create a subclass of XEdDSA and implement `_mont_pub_from_mont_priv`.")

    @classmethod
    def mont_pub_to_ed_pub(cls, mont_pub: MontPub) -> EdPub:
        """
        Args:
            mont_pub: The Montgomery public key.

        Returns:
            The (twisted) Edwards public key derived from the Montgomery public key.
        """

        wanted_size = cls._get_mont_pub_key_size()
        if len(mont_pub) != wanted_size:
            raise ValueError("The Montgomery public key must consist of {} bytes.".format(wanted_size))

        return cls._mont_pub_to_ed_pub(mont_pub)

    @staticmethod
    @abstractmethod
    def _mont_pub_to_ed_pub(mont_pub: MontPub) -> EdPub:
        """
        Args:
            mont_pub: The Montgomery public key.

        Returns:
            The (twisted) Edwards public key derived from the Montgomery public key.
        """

        raise NotImplementedError("Create a subclass of XEdDSA and implement `_mont_pub_to_ed_pub`.")

    def sign(self, msg: bytes, nonce: Optional[Nonce] = None) -> Signature:
        """
        Sign a message using the Montgomery private key stored in this XEdDSA instance.

        Args:
            msg: The message to sign.
            nonce: The nonce to use while signing. If omitted or set to :obj:`None`, a nonce is generated.

        Returns:
            The signature of the message, not including the message itself.

        Raises:
            MissingKeyException: If the Montgomery private key is not available.
        """

        if self.__mont_priv is None:
            raise MissingKeyException("Cannot sign, the Montgomery private key is not available.")

        if nonce is None:
            nonce = libnacl.randombytes(64)

        if len(nonce) != 64:
            raise ValueError("The nonce must consist of 64 bytes if given.")

        return self._sign(self.__mont_priv, msg, nonce)

    @staticmethod
    @abstractmethod
    def _sign(mont_priv: MontPriv, msg: bytes, nonce: Nonce) -> Signature:
        """
        Sign a message using a Montgomery private key.

        Args:
            mont_priv: The Montgomery private key to sign with.
            msg: The message to sign.
            nonce: The nonce to use while signing.

        Returns:
            The signature of the message, not including the message itself.
        """

        raise NotImplementedError("Create a subclass of XEdDSA and implement `_sign`.")

    def verify(self, msg: bytes, sig: Signature) -> bool:
        """
        Verify a signature using the Montgomery public key stored in this XEdDSA instance.

        Args:
            msg: The signed message.
            sig: The signature.

        Returns:
            Whether the signature is valid.
        """

        wanted_size = self._get_signature_size()
        if len(sig) != wanted_size:
            raise ValueError("The signature must consist of {} bytes.".format(wanted_size))

        return self._verify(self._mont_pub_to_ed_pub(self.__mont_pub), msg, sig)

    @staticmethod
    @abstractmethod
    def _verify(ed_pub: EdPub, msg: bytes, sig: Signature) -> bool:
        """
        Verify a signature using a (twisted) Edwards public key.

        Args:
            msg: The signed message.
            sig: The signature.
            ed_pub: The (twisted) Edwards public key.

        Returns:
            Whether the signature is valid.
        """

        raise NotImplementedError("Create a subclass of XEdDSA and implement `_verify`.")
