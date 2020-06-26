import re
from base64 import b64decode

enc = open('encrypted_db', 'r').read().replace('\n', '')
dec = b64decode(enc.decode('hex'))
print re.findall(r'flag[^.]*}', dec)
