import os

from nacl.public  import PrivateKey as Curve25519SecretKey
from nacl.public  import PublicKey  as Curve25519PublicKey
from nacl.signing import SigningKey as Ed25519SigningKey
from nacl.signing import VerifyKey  as Ed25519VerifyingKey

from nacl.exceptions import BadSignatureError

from xeddsa.implementations import XEdDSA25519

def toByteArray(string):
    return [ ord(x) for x in string ]

signing_key      = Ed25519SigningKey.generate()
verification_key = signing_key.verify_key
decryption_key   = signing_key.to_curve25519_private_key()
encryption_key   = verification_key.to_curve25519_public_key()

xeddsa = XEdDSA25519(decryption_key = bytes(decryption_key))

message       = os.urandom(100)
message_bytes = toByteArray(message)

signature        = signing_key.sign(message).signature
xeddsa_signature = xeddsa.sign(message_bytes, toByteArray(os.urandom(64)))

try:
	assert verification_key.verify(message, signature) == message
except (BadSignatureError, AssertionError):
	print "Message verification failed!"

try:
	assert xeddsa.verify(message_bytes, xeddsa_signature) == message_bytes
except (BadSignatureError, AssertionError):
	print "XEdDSA message verification failed!"

if signature == xeddsa_signature:
	print "Signed messages are equal!"
else:
	print "Signed messages are unequal."

try:
	assert verification_key.verify(message, xeddsa_signature) == message
	print "Non-XEdDSA verification key successfully verified XEdDSA signed message!"
except (BadSignatureError, AssertionError):
	print "Non-XEdDSA verification key was not abled to verify XEdDSA signed message."

try:
	assert xeddsa.verify(message_bytes, signature) == message_bytes
	print "XEdDSA verification key successfully verified Non-XEdDSA signed message!"
except (BadSignatureError, AssertionError):
	print "XEdDSA verification key was not abled to verify Non-XEdDSA signed message."
