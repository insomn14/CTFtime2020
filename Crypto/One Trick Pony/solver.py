from pwn import *
from string import printable, digits

host, port = 'chals20.cybercastors.com', 14422

p = remote(host, port)

find = 'castorsCTF{k33p_y0ur_k3y5_53cr37_4nd_d0n7_r3u53_7h3m!}'
up = '{ABCDEFGHIJKLMNOPQRSTUVWXYZ_-}'
lo = 'abcdefghijklmnopqrstuvwxyz_-}{~!@#+=|><?'+digits
try:
    while True:
        for ch in lo[::-1]:
            data = find+ch #chr(ch)
            p.sendline(data)
            msg = p.recvuntil("'\n").split()[1][2:-1]
            print(data,'->',msg)
            if len(msg) == 0:
                #find += ch#chr(ch)
                find += ch
                print 'Good :',find
                if '}' in find:
                    print 'FLAG : ',find
                    break
except KeyboardInterrupt:
    print(find)
