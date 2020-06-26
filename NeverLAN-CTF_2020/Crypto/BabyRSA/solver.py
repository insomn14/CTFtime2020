from Crypto.Util.number import long_to_bytes
from Crypto.PublicKey import RSA


def decrypt(c, n, d):
    m = long_to_bytes(pow(c, d, n))
    return m

def main(key):
    flag = []
    key = RSA.importKey(key)
    msg_list = [2193, 1745, 2164, 970, 1466, 2495, 1438, 1412, 1745, 1745, 2302, 1163, 2181, 1613, 1438, 884, 2495, 2302, 2164, 2181, 884, 2302, 1703, 1924, 2302, 1801, 1412, 2495, 53, 1337, 2217]
    for msg in msg_list:
        flag.append(decrypt(msg, key.n, key.d))
    print(''.join(flag))


if __name__ == '__main__':
    with open('private.key', 'r') as p:
        key = p.read()
    main(key)
