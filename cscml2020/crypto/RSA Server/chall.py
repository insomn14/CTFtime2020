import random

from Crypto.Util.number import bytes_to_long
from Crypto.PublicKey import RSA


FLAG: bytes = b'CENSORED'
MAX_REQUESTS: int = 2 ** 13


key = RSA.generate(1024)
encrypted_flag: int = pow(bytes_to_long(FLAG), key.e, key.n)

max_rnd: int = key.n // 37


def oracle(cipher):
    rnd_number = random.randint(7, max_rnd)
    return pow(cipher, key.d, key.n) < rnd_number


print(f"{key.n}; {key.e}; {encrypted_flag}")
for idx in range(MAX_REQUESTS):
    try:
        number = int(input("Cipher: "))
        print(f"Oracle Response: {oracle(number)}")
    except:
        break
