from typing import ClassVar, Optional, Tuple

import libnacl

MontPriv  = bytes # MONT_PRIV_KEY_SIZE bytes
MontPub   = bytes # MONT_PUB_KEY_SIZE bytes
EdPriv    = bytes # ED_PRIV_KEY_SIZE bytes
EdPub     = bytes # ED_PUB_KEY_SIZE bytes
Signature = bytes # SIGNATURE_SIZE bytes
Nonce     = bytes # 64 bytes

class MissingKeyException(Exception):
    pass

class XEdDSA:
    """
    The base class for all XEdDSA implementations.
    Do not use this class directly, use subclasses for specific key types instead.

    The :mod:`xeddsa.implementations` module ships such subclasses.
    """

    MONT_PRIV_KEY_SIZE : ClassVar[int] = NotImplemented
    MONT_PUB_KEY_SIZE  : ClassVar[int] = NotImplemented
    ED_PRIV_KEY_SIZE   : ClassVar[int] = NotImplemented
    ED_PUB_KEY_SIZE    : ClassVar[int] = NotImplemented
    SIGNATURE_SIZE     : ClassVar[int] = NotImplemented

    def __init__(self, mont_priv: Optional[MontPriv] = None, mont_pub: Optional[MontPub] = None):
        """
        Create an XEdDSA object from Montgomery key material, to encrypt AND sign data using just one
        Montgomery key pair.

        Args:
            mont_priv: The Montgomery private key.
            mont_pub: The Montgomery public key.

        If both ``mont_priv`` and ``mont_pub`` are :obj:`None`, a new key pair is generated.
        """

        cls = self.__class__

        if any(map(lambda x: x == NotImplemented, [
            cls.MONT_PRIV_KEY_SIZE,
            cls.MONT_PUB_KEY_SIZE,
            cls.ED_PRIV_KEY_SIZE,
            cls.ED_PUB_KEY_SIZE,
            cls.SIGNATURE_SIZE
        ])):
            raise NotImplementedError("Can't instantiate the XEdDSA class directly.")

        if mont_priv is None and mont_pub is None:
            mont_priv = self.generate_mont_priv()

        if mont_priv is not None and len(mont_priv) != cls.MONT_PRIV_KEY_SIZE:
            raise ValueError("The Montgomery private key must consist of MONT_PRIV_KEY_SIZE bytes if given.")

        if mont_priv is not None and mont_pub is None:
            mont_pub = self.mont_pub_from_mont_priv(mont_priv)

        if mont_pub is not None and len(mont_pub) != cls.MONT_PUB_KEY_SIZE:
            raise ValueError("The Montgomery public key must consist of MONT_PUB_KEY_SIZE bytes if given.")

        assert mont_pub is not None # sanity check, to satisfy mypy

        self.__mont_priv: Optional[MontPriv] = mont_priv
        self.__mont_pub: MontPub = mont_pub

    @classmethod
    def generate_mont_priv(cls) -> MontPriv:
        """
        Returns:
            A freshly generated Montgomery private key to be used with XEdDSA.
        """

        return cls._generate_mont_priv()

    @staticmethod
    def _generate_mont_priv() -> MontPriv:
        """
        Returns:
            A freshly generated Montgomery private key to be used with XEdDSA.
        """

        raise NotImplementedError

    @classmethod
    def mont_pub_from_mont_priv(cls, mont_priv: MontPriv) -> MontPub:
        """
        Args:
            mont_priv: The Montgomery private key.

        Returns:
            The Montgomery public key restored from the Montgomery private key.
        """

        if len(mont_priv) != cls.MONT_PRIV_KEY_SIZE:
            raise ValueError("The Montgomery private key must consist of MONT_PRIV_KEY_SIZE bytes.")

        return cls._mont_pub_from_mont_priv(mont_priv)

    @staticmethod
    def _mont_pub_from_mont_priv(mont_priv: MontPriv) -> MontPub:
        """
        Args:
            mont_priv: The Montgomery private key.

        Returns:
            The Montgomery public key restored from the Montgomery private key.
        """

        raise NotImplementedError

    @classmethod
    def mont_priv_to_ed_pair(cls, mont_priv: MontPriv) -> Tuple[EdPriv, EdPub]:
        """
        Args:
            mont_priv: The Montgomery private key.

        Returns:
            The Twisted Edwards private and public key derived from the Montgomery private key.
        """

        if len(mont_priv) != cls.MONT_PRIV_KEY_SIZE:
            raise ValueError("The Montgomery private key must consist of MONT_PRIV_KEY_SIZE bytes.")

        return cls._mont_priv_to_ed_pair(mont_priv)

    @staticmethod
    def _mont_priv_to_ed_pair(mont_priv: MontPriv) -> Tuple[EdPriv, EdPub]:
        """
        Args:
            mont_priv: The Montgomery private key.

        Returns:
            The Twisted Edwards private and public key derived from the Montgomery private key.
        """

        raise NotImplementedError

    @classmethod
    def mont_pub_to_ed_pub(cls, mont_pub: MontPub) -> EdPub:
        """
        Args:
            mont_pub: The Montgomery public key.

        Returns:
            The Twisted Edwards public key derived from the Montgomery public key.
        """

        if len(mont_pub) != cls.MONT_PUB_KEY_SIZE:
            raise ValueError("The Montgomery public key must consist of MONT_PUB_KEY_SIZE bytes.")

        return cls._mont_pub_to_ed_pub(mont_pub)

    @staticmethod
    def _mont_pub_to_ed_pub(mont_pub: MontPub) -> EdPub:
        """
        Args:
            mont_pub: The Montgomery public key.

        Returns:
            The Twisted Edwards public key derived from the Montgomery public key.
        """

        raise NotImplementedError

    def sign(self, data: bytes, nonce: Optional[Nonce] = None) -> Signature:
        """
        Sign data using the Montgomery private key stored in this XEdDSA instance.

        Args:
            data: The data to sign.
            nonce: The nonce to use while signing. If omitted or set to :obj:`None`, a nonce is generated.

        Returns:
            The signature of the data, not including the data itself.

        Raises:
            MissingKeyException: If the Montgomery private key is not available.
        """

        if self.__mont_priv is None:
            raise MissingKeyException("Cannot sign, the Montgomery private key is not available.")

        if nonce is None:
            nonce = libnacl.randombytes(64)

        if len(nonce) != 64:
            raise ValueError("The nonce must consist of 64 bytes if given.")

        ed_priv, ed_pub = self._mont_priv_to_ed_pair(self.__mont_priv)

        return self._sign(data, nonce, ed_priv, ed_pub)

    @staticmethod
    def _sign(data: bytes, nonce: Nonce, ed_priv: EdPriv, ed_pub: EdPub) -> Signature:
        """
        Sign data using the Twisted Edwards key pair.

        Args:
            data: The data to sign.
            nonce: The nonce to use while signing.
            ed_priv: The Twisted Edwards private key to sign with.
            ed_pub: The Twisted Edwards public key to sign with.

        Returns:
            The signature of the data, not including the data itself.
        """

        raise NotImplementedError

    def verify(self, data: bytes, signature: Signature) -> bool:
        """
        Verify a signature using the Montgomery public key stored in this XEdDSA instance.

        Args:
            data: The data.
            signature: The signature.

        Returns:
            Whether the signature is valid.
        """

        if len(signature) != self.__class__.SIGNATURE_SIZE:
            raise ValueError("The signature must consist of SIGNATURE_SIZE bytes.")

        return self._verify(data, signature, self._mont_pub_to_ed_pub(self.__mont_pub))

    @staticmethod
    def _verify(data: bytes, signature: Signature, ed_pub: EdPub) -> bool:
        """
        Verify a signature using a Twisted Edwards public key.

        Args:
            data: The data.
            signature: The signature.
            ed_pub: The Twisted Edwards public key.

        Returns:
            Whether the signature is valid.
        """

        raise NotImplementedError
