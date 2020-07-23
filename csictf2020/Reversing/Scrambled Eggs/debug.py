import random 
import sys


map = ['v', 'r', 't', 'p', 'w', 'g', 'n', 'c', 'o', 'b', 'a', 'f', 'm', 'i', 'l', 'u', 'h', 'z', 'd', 'q', 'j', 'y', 'x', 'e', 'k', 's']

flag = 'csictf{this_is_a_fake_flagg}'
flag = flag.replace('{','a')
flag = flag.replace('}','a')
flag = flag.replace('_','b')
key1 = 'shikka_is_mine'
key1 = key1.replace('_','b')


if(len(flag) != 28 or len(key1) != 14):
    print('EXIT!')
    exit()
    
flag = list(flag)
key1 = list(key1)


# def enc1(text):
#     n = random.randint(0,sys.maxsize%28)
#     return text[n:] + text[:n]
enc1 = lambda text, n=random.randint(0,7) : text[n:] + text[:n]

flag = enc1(flag)

def enc2(text):
    temp = ''
    for i in text:
        temp += map[ord(i)-ord('a')]
    return temp

key2 = enc2(enc2(key1))
key2 = list(key2)

# print('-'*25)
# print(f'KEY2 : {"".join(key2)}')
# print(f'FLAG : {"".join(flag)}')
# print(f'KEY1 : {"".join(key1)}')
for _ in range(2):
    for i in range(14):
        TEMP1 = flag[i]
        flag[i] = flag[ (ord(key1[i]) - ord('a')) % 28 ] 
        flag[ (ord(key1[i]) - ord('a')) % 28 ]  = TEMP1

        TEMP2 = key1[i]
        key1[i] = key1[ (ord(key2[i]) - ord('a')) % 14 ] 
        key1[ (ord(key2[i]) - ord('a')) % 14 ] = TEMP2
    # print(f'key1 : {"".join(key1)}')

    for i in range(14,28):
        TEMP1 = flag[i]
        flag[i] = flag[ (ord(key2[i-14]) - ord('a')) % 28 ] 
        flag[ (ord(key2[i-14]) - ord('a')) % 28 ] = TEMP1

        TEMP2 = key2[i-14]
        key2[i-14] = key2[ (ord(key1[i-14]) - ord('a')) % 14 ] 
        key2[ (ord(key1[i-14]) - ord('a')) % 14 ] = TEMP2
        # print(key2, i-14, (ord(key1[i-14]) - ord('a')) % 14)
    # print(f'key2 : {"".join(key2)}')

# print('-'*25)
# print(f'FLAG : {"".join(flag)}')
# print(f'KEY1 : {"".join(key1)}')
# print(f'KEY2 : {"".join(key2)}')
# flag = enc1(enc1(enc1(enc2(flag))))
# print('Encrypted flag = '+flag)
# exit()    
l = random.sample([key1, key2], 2) # acak posisi doang
key1 = l[0]
key2 = l[1]

# print(key1)
# print(key2)

k = ''
for i in range(14):
    k += random.choice(map)
k = list(k)

# print(''.join(k))
key2 = k + key2
for i in range(14):
    a = ord(k[i]) - ord('a') + ord(key2[i+14])
    if a > 122:
        a = a % 122
        a = a + 97
    key2[i+14] = chr(a)


flag = ''.join(flag)
key1 = ''.join(key1)
key2 = ''.join(key2)
 
key2 = enc2(key2)
flag = enc1(enc1(enc1(enc2(flag))))

# print('Encrytped key1 = '+key1)
# print('Encrypted key2 = '+key2)
# print('Encrypted flag = '+flag)


# --------------------------------------- SOLUTION ---------------------------------------

inv_map = ['k', 'j', 'h', 's', 'x', 'l', 'f', 'q', 'n', 'u', 'y', 'o', 'm', 'g', 'i', 'd', 't', 'b', 'z', 'c', 'p', 'a', 'e', 'w', 'v', 'r']

def inv_enc2(text):
    temp = ''
    for i in text:
        temp += inv_map[ord(i)-ord('a')]
    return temp

# [+] RECOVERY KEY :
key1 = EncrytpedKey1 = list('xtfsyhhlizoiyx')
EncryptedKey2 = 'eudlqgluduggdluqmocgyukhbqkx'
EncryptedFlag = 'lvvrafwgtocdrdzfdqotiwvrcqnd'
#
# RECOVERY KEY2 :
key2 = inv_enc2(EncryptedKey2)
# print(key2)
#
from string import ascii_lowercase
key2 = list(key2)
k = key2[:14]
# print(f"k : {''.join(k)}")
rkey2 = []
i = 0
while len(rkey2) != 14:
    for ch in ascii_lowercase:
        a = ord(k[i]) - ord('a') + ord(ch)
        if a > 122:
            a = a % 122
            a = a + 97
        if chr(a) == key2[i+14]:
            rkey2.append(ch)
            i += 1
            break
# KEY2 SUCCESSFULY RECOVERY
print(f"key1 : {''.join(key1)}")    # xtfsyhhlizoiyx
print(f"key2 : {''.join(rkey2)}")   # rettnahagbeogi

# SWITCH POSITION
print('[1]'+'-'*25)
tmp = rkey2
rkey2 = key1
key1 = tmp
print(f"key1 : {''.join(key1)}")    # rettnahagbeogi
print(f"key2 : {''.join(rkey2)}")   # xtfsyhhlizoiyx
# -------------------------------------
# RECOVERY KEY1 & KEY2 POSITION
for _ in range(2):
    for i in range(14):
        TEMP2 = rkey2[13-i]
        rkey2[13-i] = rkey2[ (ord(key1[13-i]) - ord('a')) % 14 ] 
        rkey2[ (ord(key1[13-i]) - ord('a')) % 14 ] = TEMP2

    for i in range(14):
        TEMP2 = key1[13-i]
        key1[13-i] = key1[ (ord(rkey2[13-i]) - ord('a')) % 14 ] 
        key1[ (ord(rkey2[13-i]) - ord('a')) % 14 ] = TEMP2

print('[2]'+'-'*25)
print(f"key1 : {''.join(key1)}")    # togetherbagain
print(f"key2 : {''.join(rkey2)}")   # hfixhtxszyiylo
# KEY1 & KEY2 POSITION SUCCESSFULY RECOVERY
# -------------------------------------
# RECOVERY KEY2 MAP
print('[3]'+'-'*25)
rkey2 = inv_enc2(inv_enc2(rkey2))
key1 = ''.join(key1)
rkey2 = ''.join(rkey2)
assert key1 == rkey2
KEY = key1.replace('b', '_')
print(f'KEY : {KEY}')

# -------------------------------- [+] RECOVERY FLAG : -------------------------------- 
import numpy 

inv_enc1 = lambda text,n: ''.join(numpy.roll(list(text),n))

# enc_flag = []
 
# for i in range(7):
#     for j in range(7):
#         for k in range(7):
#             tmp = inv_enc1(inv_enc1(inv_enc1('lvvrafwgtocdrdzfdqotiwvrcqnd',k), j), i)
#             if tmp not in enc_flag:
#                 print(tmp)
#                 enc_flag.append(tmp)
# 19 POSIBILITY 
# enc_flag = ['lvvrafwgtocdrdzfdqotiwvrcqnd', 'dlvvrafwgtocdrdzfdqotiwvrcqn', 'ndlvvrafwgtocdrdzfdqotiwvrcq', 'qndlvvrafwgtocdrdzfdqotiwvrc', 'cqndlvvrafwgtocdrdzfdqotiwvr', 'rcqndlvvrafwgtocdrdzfdqotiwv', 'vrcqndlvvrafwgtocdrdzfdqotiw', 'wvrcqndlvvrafwgtocdrdzfdqoti', 'iwvrcqndlvvrafwgtocdrdzfdqot', 'tiwvrcqndlvvrafwgtocdrdzfdqo', 'otiwvrcqndlvvrafwgtocdrdzfdq', 'qotiwvrcqndlvvrafwgtocdrdzfd', 'dqotiwvrcqndlvvrafwgtocdrdzf', 'fdqotiwvrcqndlvvrafwgtocdrdz', 'zfdqotiwvrcqndlvvrafwgtocdrd', 'dzfdqotiwvrcqndlvvrafwgtocdr', 'rdzfdqotiwvrcqndlvvrafwgtocd', 'drdzfdqotiwvrcqndlvvrafwgtoc', 'cdrdzfdqotiwvrcqndlvvrafwgto']

# for i, enc in enumerate(enc_flag):
#     enc_flag[i] = inv_enc2(enc)
 
# RESUTL AFTER inv_enc2(enc_flag) 
print('[4]'+'+'*25)
enc_flag = ['oaabklefcihsbsrlsticneabhtgs', 'soaabklefcihsbsrlsticneabhtg', 'gsoaabklefcihsbsrlsticneabht', 'tgsoaabklefcihsbsrlsticneabh', 'htgsoaabklefcihsbsrlsticneab', 'bhtgsoaabklefcihsbsrlsticnea', 'abhtgsoaabklefcihsbsrlsticne', 'eabhtgsoaabklefcihsbsrlsticn', 'neabhtgsoaabklefcihsbsrlstic', 'cneabhtgsoaabklefcihsbsrlsti', 'icneabhtgsoaabklefcihsbsrlst', 'ticneabhtgsoaabklefcihsbsrls', 'sticneabhtgsoaabklefcihsbsrl', 'lsticneabhtgsoaabklefcihsbsr', 'rlsticneabhtgsoaabklefcihsbs', 'srlsticneabhtgsoaabklefcihsb', 'bsrlsticneabhtgsoaabklefcihs', 'sbsrlsticneabhtgsoaabklefcih', 'hsbsrlsticneabhtgsoaabklefci']

for flag in enc_flag:
    flag = list(flag)
    key1 = list('rettnahagbeogi')
    key2 = list('xtfsyhhlizoiyx')
    for _ in range(2):
        for i in range(14,28):
            TEMP2 = key2[13-i]
            key2[13-i] = key2[ (ord(key1[13-i]) - ord('a')) % 14 ] 
            key2[ (ord(key1[13-i]) - ord('a')) % 14 ] = TEMP2

            TEMP1 = flag[41-i]
            flag[41-i] = flag[ (ord(key2[13-i]) - ord('a')) % 28 ] 
            flag[ (ord(key2[13-i]) - ord('a')) % 28 ] = TEMP1

        for i in range(14):
            TEMP2 = key1[13-i]
            key1[13-i] = key1[ (ord(key2[13-i]) - ord('a')) % 14 ] 
            key1[ (ord(key2[13-i]) - ord('a')) % 14 ] = TEMP2

            TEMP1 = flag[13-i]
            flag[13-i] = flag[ (ord(key1[13-i]) - ord('a')) % 28 ] 
            flag[ (ord(key1[13-i]) - ord('a')) % 28 ]  = TEMP1

    for i in range(7):
        get = "".join(inv_enc1(flag,i))
        get = get.replace('a', '{')
        get = get.replace('b', '_')
        if 'csictf{' in get:
            print(f'Found : {get}')

# FOUND : csictf}}llbthebkingsbhorses} -> csictf{allbthebkingsbhorses}
# FLAG : 'csictf{all_the_kings_horses}'