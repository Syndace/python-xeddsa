import os

from nacl.public  import PrivateKey as Curve25519SecretKey
from nacl.public  import PublicKey  as Curve25519PublicKey
from nacl.signing import SigningKey as Ed25519SigningKey
from nacl.signing import VerifyKey  as Ed25519VerifyingKey

from nacl.exceptions import BadSignatureError

from xeddsa import mont_priv_to_ed_pair

signing_key      = Ed25519SigningKey.generate()
verification_key = signing_key.verify_key
decryption_key   = signing_key.to_curve25519_private_key()
encryption_key   = verification_key.to_curve25519_public_key()

xeddsa_signing_key, xeddsa_verification_key = mont_priv_to_ed_pair([ ord(x) for x in bytes(decryption_key) ])
xeddsa_signing_key      = Ed25519SigningKey(xeddsa_signing_key)
xeddsa_verification_key = Ed25519VerifyingKey(xeddsa_verification_key)

message = os.urandom(100)

if bytes(xeddsa_signing_key) == bytes(signing_key):
    print "Same private keys"
else:
    print "Different private keys"

if bytes(xeddsa_verification_key) == bytes(verification_key):
    print "Same public keys"
else:
    print "Different public keys"

signed_message = signing_key.sign(message)
xeddsa_signed_message = xeddsa_signing_key.sign(message)

try:
	assert verification_key.verify(signed_message) == message
except (BadSignatureError, AssertionError):
	print "Message verification failed!"

try:
	assert xeddsa_verification_key.verify(xeddsa_signed_message) == message
except (BadSignatureError, AssertionError):
	print "XEdDSA message verification failed!"

if signed_message == xeddsa_signed_message:
	print "Signed messages are equal!"
else:
	print "Signed messages are unequal."

try:
	assert verification_key.verify(xeddsa_signed_message) == message
	print "Non-XEdDSA verification key successfully verified XEdDSA signed message!"
except (BadSignatureError, AssertionError):
	print "Non-XEdDSA verification key was not abled to verify XEdDSA signed message."

try:
	assert xeddsa_verification_key.verify(signed_message) == message
	print "XEdDSA verification key successfully verified Non-XEdDSA signed message!"
except (BadSignatureError, AssertionError):
	print "XEdDSA verification key was not abled to verify Non-XEdDSA signed message."
