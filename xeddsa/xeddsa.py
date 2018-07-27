# I can't believe they moved reduce from the global space :(
from functools import reduce

import os

def bytesToString(data):
    return bytes(bytearray(data))

def toBytes(data):
    def toInt(x):
        try:
            return ord(x)
        except TypeError:
            return x

    try:
        return [ toInt(x) for x in data ]
    except TypeError:
        return data

class XEdDSA(object):
    def __init__(self, decryption_key = None, encryption_key = None):
        self._decryption_key = toBytes(decryption_key)
        self._encryption_key = toBytes(encryption_key)

        if self._decryption_key and not self._encryption_key:
            self._encryption_key = self.__class__._restoreEncryptionKey(self._decryption_key)

    def sign(self, message, nonce = None):
        if not self._decryption_key:
            raise MissingKeyException("Cannot sign using this XEdDSA instance, Montgomery decryption key missing")

        message = toBytes(message)

        if nonce == None:
            nonce = os.urandom(64)

        nonce = toBytes(nonce)

        return self._sign(message, nonce, *self.__class__._mont_priv_to_ed_pair(self._decryption_key))

    def verify(self, message, signature):
        if not self._encryption_key:
            raise MissingKeyException("Cannot verify using this XEdDSA instance, Montgomery encryption key missing")

        message = toBytes(message)
        signature = toBytes(signature)

        return self._verify(message, signature, self.__class__._mont_pub_to_ed_pub(self._encryption_key))

    @classmethod
    def _restoreEncryptionKey(cls, decryption_key):
        """
        Restore the encryption key from a given Montgomery decryption key and return it.
        """

        raise NotImplementedError

    @classmethod
    def _sign(cls, message, nonce, verification_key, signing_key):
        """
        Return the detached signature.
        """

        raise NotImplementedError

    @classmethod
    def _verify(cls, message, signature, verification_key):
        """
        Return a boolean indicating verification success.
        """

        raise NotImplementedError

    @classmethod
    def _mont_priv_to_ed_pair(cls, mont_priv):
        """
        Derive a twisted Edwards key pair from a Montgomery private key.
        Return public key, private key.
        """

        raise NotImplementedError

    @classmethod
    def _mont_pub_to_ed_pub(cls, mont_pub):
        """
        Derive a twisted Edwards public key from a Montgomery public key.
        """

        raise NotImplementedError
