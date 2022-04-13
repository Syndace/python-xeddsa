from .version import __version__
from .project import project

from .bindings import (
    Priv, PRIV_SIZE,
    Seed, SEED_SIZE,
    Curve25519Pub, CURVE_25519_PUB_SIZE,
    Ed25519Pub, ED_25519_PUB_SIZE,
    Ed25519Signature, ED_25519_SIGNATURE_SIZE,
    Nonce, NONCE_SIZE,
    SharedSecret, SHARED_SECRET_SIZE,

    XEdDSAException,

    ed25519_priv_sign,
    ed25519_seed_sign,
    ed25519_verify,

    curve25519_pub_to_ed25519_pub,
    ed25519_pub_to_curve25519_pub,

    priv_to_curve25519_pub,
    priv_to_ed25519_pub,
    seed_to_ed25519_pub,

    priv_force_sign,
    seed_to_priv,

    x25519
)


# Fun:
# https://github.com/PyCQA/pylint/issues/6006
# https://github.com/python/mypy/issues/10198
__all__ = [  # pylint: disable=unused-variable
    # .version
    "__version__",

    # .project
    "project",

    # .bindings
    "Priv", "PRIV_SIZE",
    "Seed", "SEED_SIZE",
    "Curve25519Pub", "CURVE_25519_PUB_SIZE",
    "Ed25519Pub", "ED_25519_PUB_SIZE",
    "Ed25519Signature", "ED_25519_SIGNATURE_SIZE",
    "Nonce", "NONCE_SIZE",
    "SharedSecret", "SHARED_SECRET_SIZE",

    "XEdDSAException",

    "ed25519_priv_sign",
    "ed25519_seed_sign",
    "ed25519_verify",

    "curve25519_pub_to_ed25519_pub",
    "ed25519_pub_to_curve25519_pub",

    "priv_to_curve25519_pub",
    "priv_to_ed25519_pub",
    "seed_to_ed25519_pub",

    "priv_force_sign",
    "seed_to_priv",

    "x25519"
]
