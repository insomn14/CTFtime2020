from Crypto.Util.number import long_to_bytes
from Crypto.PublicKey import RSA

c = 32949
f = open('keypair.pem').read()

key = RSA.importKey(f)

m = pow(c, key.n, key.d)
print(m)