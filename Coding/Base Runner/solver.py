import binascii
from pwn import *
from Crypto.Util.number import long_to_bytes as ltb


convbin = lambda x : binascii.unhexlify('%x' % x)


host, port = 'chals20.cybercastors.com', 14430

r = remote(host, port)

print (r.recvuntil('ready.\n'))
r.sendline('')

data = r.recvuntil('\n').split()
n = ltb(int(str(''.join([convbin(int(bins, 2)) for bins in data]).replace(' ', '')),16))
log.info('DATA : {}'.format(n))

r.sendline(n)

print (r.recv())

r.interactive()