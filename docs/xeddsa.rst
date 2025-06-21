xeddsa.bindings
===============

Formats
-------

The library follows following standards for serialization formats:

* Curve25519/Ed25519 private keys: 32 bytes scalar value. No specific format. Clamped before every use as per `RFC 7748, section 5 "The X25519 and X448 Functions" <https://www.rfc-editor.org/rfc/rfc7748.html#section-5>`_.
* Curve25519/Ed25519 seeds: 32 bytes. No specific format. The private key is derived from the seed using SHA-512 as per `RFC 8032, section 3.2 "Keys" <https://www.rfc-editor.org/rfc/rfc8032.html#section-3.2>`_.
* Curve25519 public keys: 32 bytes, the little-endian encoding of the u coordinate as per `RFC 7748, section 5 "The X25519 and X448 Functions" <https://www.rfc-editor.org/rfc/rfc7748.html#section-5>`_.
* Ed25519 public keys: 32 bytes, the little-endian encoding of the y coordinate with the sign bit of the x coordinate stored in the most significant bit as per `RFC 8032, section 3.2 "Keys" <https://www.rfc-editor.org/rfc/rfc8032.html#section-3.2>`_.
* Ed25519 signatures: 64 bytes, following the format defined in `RFC 8032, section 3.3 "Sign" <https://www.rfc-editor.org/rfc/rfc8032.html#section-3.3>`_.

API
---

.. automodule:: xeddsa.bindings
    :members:
    :exclude-members: Priv, Seed, Curve25519Pub, Ed25519Pub, Ed25519Signature, Nonce, SharedSecret
    :private-members:
    :undoc-members:
    :member-order: bysource
    :show-inheritance:

Type Aliases
============

.. autoclass:: xeddsa.bindings.Priv
.. autoclass:: xeddsa.bindings.PRIV_SIZE

.. autoclass:: xeddsa.bindings.Seed
.. autoclass:: xeddsa.bindings.SEED_SIZE

.. autoclass:: xeddsa.bindings.Curve25519Pub
.. autoclass:: xeddsa.bindings.CURVE_25519_PUB_SIZE

.. autoclass:: xeddsa.bindings.Ed25519Pub
.. autoclass:: xeddsa.bindings.ED_25519_PUB_SIZE

.. autoclass:: xeddsa.bindings.Ed25519Signature
.. autoclass:: xeddsa.bindings.ED_25519_SIGNATURE_SIZE

.. autoclass:: xeddsa.bindings.Nonce
.. autoclass:: xeddsa.bindings.NONCE_SIZE

.. autoclass:: xeddsa.bindings.SharedSecret
.. autoclass:: xeddsa.bindings.SHARED_SECRET_SIZE
