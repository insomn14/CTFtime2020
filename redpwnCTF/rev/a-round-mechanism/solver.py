#!/usr/bin/python3

from itertools import permutations
from string import printable

xor = lambda x: ''.join([chr(ord(i)^18) for i in x])

def ENCrypt(a1, a2, a3):
	while a2 != a3:
		v4 = (ord(a1[a2-1]) >> 1) + (ord(a1[a2]) << 1)
		a1[a2] = chr( (v4 >> (v4 >> 7)) - 1 )
		a2 += 1
	return a1

def find(k, f):
	found = []
	for ch in printable:
		tmp = list(k+ch)
		tmp = ENCrypt(tmp, 1, len(tmp))
		if tmp[1] == f:
			print(f'- possibility : {ch}')
			found.append(ch)
	return found		

enc_flag = "4CB\\y}@vxI^{~kFfe}B@et"
know_key = str(input("Know 1st char : "))
find_key = str(input("Restore 2nd char: "))
possibility = find(know_key, find_key)

for pos in possibility:
	data = list(know_key + pos)
	tmp = ''.join(data)
	while len(data) != len(enc_flag):
		for ch in printable:
			tmp = list(tmp+ch)
			ENCrypt(tmp, 1, len(tmp))
			if all(enc_flag[i]==j for i,j in enumerate(tmp)):
				data.append(ch)
				tmp = ''.join(data)
				break
			else:
				tmp = ''.join(data)
	print('-'*35)
	print(f'Result - {pos} : {tmp}')
	check = ''.join((ENCrypt(list(data),1,len(data)))) == enc_flag
	print(f"Compare key : {check}")
	if (check): 
		print(f"Key found : {xor(tmp)}")
	else:
		print("Key not found")
