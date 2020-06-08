from pwn import *
from base64 import b64decode

def main():
    r = remote('challenges.neverlanctf.com', 1120)
    while(1):
        try:
            print '+'*90
            print r.recvline()
            print r.recvuntil(': ')
            bases = r.recv()
            log.info(bases)
            r.send(b64decode(bases).decode('utf-8'))
        except:
            print '-'*90
            test = r.recv()
            if 'flag' in test:
                log.info(test)
                exit()
    r.interactive()

if __name__ == '__main__':
    main()
