# 804844a:       b9 0b 00 00 00          mov    ecx,0xb
# 804844f:       b8 41 00 00 00          mov    eax,0x41
# 8048454:       31 da                   xor    edx,ebx
# 8048456:       b9 16 00 00 00          mov    ecx,0x16
# 804845b:       b8 57 00 00 00          mov    eax,0x57
# 8048460:       bb 00 00 00 00          mov    ebx,0x0
# 8048465:       83 c3 10                add    ebx,0x10
# 8048468:       89 d9                   mov    ecx,ebx
# 804846a:       b8 79 00 00 00          mov    eax,0x79
# 804846f:       31 d2                   xor    edx,edx
# 8048471:       ba 01 00 00 00          mov    edx,0x1
# 8048476:       c1 e2 04                shl    edx,0x4
# 8048479:       b9 0a 00 00 00          mov    ecx,0xa
# 804847e:       09 d1                   or     ecx,edx
# 8048480:       b8 64 00 00 00          mov    eax,0x64
# 8048485:       b9 0d 00 00 00          mov    ecx,0xd
# 804848a:       b8 64 00 00 00          mov    eax,0x64
# 804848f:       b9 03 00 00 00          mov    ecx,0x3
# 8048494:       b8 47 00 00 00          mov    eax,0x47
# 8048499:       b9 14 00 00 00          mov    ecx,0x14
# 804849e:       b8 6c 00 00 00          mov    eax,0x6c
# 80484a3:       b9 10 00 00 00          mov    ecx,0x10
# 80484a8:       81 e1 ff 00 00 00       and    ecx,0xff
# 80484ae:       83 c1 02                add    ecx,0x2
# 80484b1:       b8 65 00 00 00          mov    eax,0x65
# 80484b6:       b9 0c 00 00 00          mov    ecx,0xc
# 80484bb:       b8 6e 00 00 00          mov    eax,0x6e
# 80484c0:       b9 02 00 00 00          mov    ecx,0x2
# 80484c5:       b8 41 00 00 00          mov    eax,0x41
# 80484ca:       b9 13 00 00 00          mov    ecx,0x13
# 80484cf:       b8 6c 00 00 00          mov    eax,0x6c
# 80484d4:       b9 09 00 00 00          mov    ecx,0x9
# 80484d9:       b8 55 00 00 00          mov    eax,0x55
# 80484de:       b9 17 00 00 00          mov    ecx,0x17
# 80484e3:       b8 6f 00 00 00          mov    eax,0x6f
# 80484e8:       b9 0a 00 00 00          mov    ecx,0xa
# 80484ed:       b8 70 00 00 00          mov    eax,0x70
# 80484f2:       b9 19 00 00 00          mov    ecx,0x19
# 80484f7:       b8 6c 00 00 00          mov    eax,0x6c
# 80484fc:       b9 06 00 00 00          mov    ecx,0x6
# 8048501:       b8 61 00 00 00          mov    eax,0x61
# 8048506:       31 c9                   xor    ecx,ecx
# 8048508:       b8 46 00 00 00          mov    eax,0x46
# 804850d:       b9 1b 00 00 00          mov    ecx,0x1b
# 8048512:       b8 7d 00 00 00          mov    eax,0x7d
# 8048517:       b9 11 00 00 00          mov    ecx,0x11
# 804851c:       b8 48 00 00 00          mov    eax,0x48
# 8048521:       b9 01 00 00 00          mov    ecx,0x1
# 8048526:       b8 4c 00 00 00          mov    eax,0x4c
# 804852b:       b9 18 00 00 00          mov    ecx,0x18
# 8048530:       ba 2d 00 00 00          mov    edx,0x2d
# 8048535:       d1 e2                   shl    edx,1
# 8048537:       01 ca                   add    edx,ecx
# 8048539:       89 d0                   mov    eax,edx
# 804853b:       b9 15 00 00 00          mov    ecx,0x15
# 8048540:       b8 6f 00 00 00          mov    eax,0x6f
# 8048545:       b9 04 00 00 00          mov    ecx,0x4
# 804854a:       b8 7b 00 00 00          mov    eax,0x7b
# 804854f:       b9 07 00 00 00          mov    ecx,0x7
# 8048554:       b8 72 00 00 00          mov    eax,0x72
# 8048559:       b9 08 00 00 00          mov    ecx,0x8
# 804855e:       b8 6d 00 00 00          mov    eax,0x6d
# 8048563:       b9 0f 00 00 00          mov    ecx,0xf
# 8048568:       b8 61 00 00 00          mov    eax,0x61
# 804856d:       b9 0e 00 00 00          mov    ecx,0xe
# 8048572:       b8 53 00 00 00          mov    eax,0x53
# 8048577:       b9 05 00 00 00          mov    ecx,0x5
# 804857c:       b8 57 00 00 00          mov    eax,0x57

flag = [0]*28

flag[0xb] = 0x41
flag[0x16] = 0x57
flag[0x10] = 0x79
flag[((1 << 4) | 0xa)] = 0x64
flag[0xd] = 0x64
flag[0x3] = 0x47
flag[0x14] = 0x6c
flag[0x12] = 0x65
flag[0xc] = 0x6e
flag[0x2] = 0x41
flag[0x13] = 0x6c
flag[0x9] = 0x55
flag[0x17] = 0x6f
flag[0xa] = 0x70
flag[0x19] = 0x6c
flag[0x6] = 0x61
flag[0x0] = 0x46
flag[0x1b] = 0x7d
flag[0x11] = 0x48
flag[0x1] = 0x4c
flag[0x18] = (0x2d << 1) + 24
flag[0x15] = 0x6f
flag[0x4] = 0x7b
flag[0x7] = 0x72
flag[0x8] = 0x6d
flag[0xf] = 0x61
flag[0xe] = 0x53
flag[0x5] = 0x57

print(''.join(chr(i) for i in flag).replace('FLAG', 'ISITDTU'))