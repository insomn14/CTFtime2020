from Crypto.PublicKey import RSA
from Crypto.Util.number import long_to_bytes as ltb

c = 1415060907955076984980255543080831671725408472748
private = open('keypair.pem').read()
key = RSA.importKey(private)

print(ltb(pow(c, key.d, key.n))[::-1])