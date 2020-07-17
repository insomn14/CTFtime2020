from pwn import *

host, port = 'chals20.cybercastors.com', 14421

r = remote(host, port)
ori = 'ST3YC4LM4NDK33PH4PPYH4CK1NGUNT1LD3ADB33F133337'
inp = 'LPC13YKYUD3S441D13DPGA3TNPN33MHKLFC3HNB3434T37'
print r.recvuntil(': ')
r.sendline('2')
print r.recvuntil('\n')
flag = str(r.recvuntil('\n').replace('\n', '').split(' ')[-1])
log.info('LEAK : {}'.format(flag))

r.sendline('1')
r.sendlineafter('?:', inp)
enc = str(r.recvline().split(' ')[-1])
log.info('MSG: {}'.format(enc))

i = 0
# while True:
#     r.sendline('1')
#     r.sendlineafter('?:', enc)
#     enc = str(r.recvline().replace('\n', '').split(' ')[-1])
#     log.info('{} MSG: {}'.format(i, enc))
#     i += 1
#     if enc == ori:
#         print(enc,':',ori)
#         break
# 
# print(inp,':',enc)
# print(inp == enc)

leak = flag
while True:
    r.sendline('1')
    r.sendlineafter('?:', leak)
    leak = str(r.recvline().replace('\n', '').split(' ')[-1])
    log.info('{} MSG: {}'.format(i, leak))
    i += 1
    if leak == flag:
        print(leak,':',flag)
        break

r.interactive()
