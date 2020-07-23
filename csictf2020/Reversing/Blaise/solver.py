#!/usr/bin/python
import sys
from pwn import *

def f(a1):
	v3 = 1;
	i = 2
	while (i <= a1):
		v3 = i * v3
		i += 1
	return v3

def C(a1, a2):
	v1 = f(a1)
	v2 = f(a2)
	v3 =  f(a1 - a2)
	return v1 // (v2 * v3)

def main(sh):
	i = 0
	recv = int(sh.recvline().strip())
	log.info(recv)
	while i <= recv:
		data = str(C(recv,i))
		log.info(data)
		sh.sendline(data)
		i += 1
	log.info(sh.recv())

if __name__ == '__main__':
	if len(sys.argv) > 1:
		sh = process('./blaise')
	else:
		sh = remote('chall.csivit.com', 30808)
	exit(main(sh))