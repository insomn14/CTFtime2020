#!/usr/bin/python3
import sys
from pwn import *

def func1(a1, a2):
    v4 = 0
    i = 1
    while a1 >= i or a2 >= i:
        if (a1 % i) == 0 and (a2 % i) == 0:
            v4 = i
        i += 1
    return v4

def func2(a1):
    if a1 != 0:
        result = a1 * func2(a1 - 1)
    else:
        result = 1
    return result

def main(sh):
    while True:
        recv = sh.recvline().strip()
        if b'fun()' not in recv:
            v13, v12 = [int(i) for i in recv.split(b' ')] 
            res = func2(func1(v13, v12) + 3)
            log.info(f'{v13} | {v12} : {res}')
            sh.sendline(str(res))
        else:
            log.info(recv)
            log.info(sh.recvall())
            break

if __name__ == '__main__':
    if len(sys.argv) > 1:
        sh = process('./RickNMorty')
    else:
        sh = remote('chall.csivit.com', 30827)
    exit(main(sh))