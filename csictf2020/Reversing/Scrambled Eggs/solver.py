import random 
import sys
from string import ascii_lowercase

inv_map = ['k', 'j', 'h', 's', 'x', 'l', 'f', 'q', 'n', 'u', 'y', 'o', 'm', 'g', 'i', 'd', 't', 'b', 'z', 'c', 'p', 'a', 'e', 'w', 'v', 'r']

def inv_enc2(text):
	temp = ''
	for i in text:
		temp += inv_map[ord(i)-ord('a')]
	return temp


# [+] RECOVERY KEYS :
key1 = EncrytpedKey1 = list('xtfsyhhlizoiyx')
EncryptedKey2 = 'eudlqgluduggdluqmocgyukhbqkx'
EncryptedFlag = 'lvvrafwgtocdrdzfdqotiwvrcqnd'

# RECOVERY KEY2 :
key2 = list(inv_enc2(EncryptedKey2))
k = key2[:14]
print(f"key2 : {''.join(key2)}")
print(f"k : {''.join(k)}")

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
print('-'*25)
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

print('-'*25)
print(f"key1 : {''.join(key1)}")    # togetherbagain
print(f"key2 : {''.join(rkey2)}")   # hfixhtxszyiylo
# KEY1 & KEY2 POSITION SUCCESSFULY RECOVERY
# -------------------------------------
# RECOVERY KEY2 MAP
print('-'*25)
rkey2 = inv_enc2(inv_enc2(rkey2))
key1 = ''.join(key1)
rkey2 = ''.join(rkey2)

assert key1 == rkey2

KEY = key1.replace('b', '_')
print(f'FOUND KEY : {KEY}')
print('-'*25)
# -------------------------------- [+] RECOVERY FLAG : -------------------------------- 
import numpy 

inv_enc1 = lambda text,n: ''.join(numpy.roll(list(text),n))

 
enc_flag = []
for i in range(7):
	for j in range(7):
		for k in range(7):
			tmp = inv_enc1(inv_enc1(inv_enc1('lvvrafwgtocdrdzfdqotiwvrcqnd',k), j), i)
			if tmp not in enc_flag:
				enc_flag.append(tmp)

for i, enc in enumerate(enc_flag):
	enc_flag[i] = inv_enc2(enc)
 
# RESUTL AFTER inv_enc2(enc_flag) 
print('+'*25)

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
			print(f'FOUND FLAG : {get}')

# FLAG : 'csictf{all_the_kings_horses}'