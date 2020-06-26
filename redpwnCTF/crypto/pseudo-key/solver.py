#!/usr/bin/env python3

from string import ascii_lowercase

chr_to_num = {c: i for i, c in enumerate(ascii_lowercase)}
num_to_chr = {i: c for i, c in enumerate(ascii_lowercase)}

def decrypt(ctxt, key):
	ctxt = ctxt.lower()
	key = ''.join(key[i % len(key)] for i in range(len(ctxt))).lower()
	ptxt = ''
	i = 0
	try:
		while len(ptxt) < len(ctxt):
			for ch in ascii_lowercase:
				if ctxt[i] == '_':
					ptxt += '_'
					i+=1
					continue
				x = chr_to_num[ch]
				y = chr_to_num[key[i]]
				tmp = num_to_chr[(x + y) % 26]
				if tmp == ctxt[i]:
					ptxt += ch
					i+=1
					break
		return ptxt
	except IndexError:
		return ptxt

def encrypt(ptxt, key):
	ptxt = ptxt.lower()
	key = ''.join(key[i % len(key)] for i in range(len(ptxt))).lower()
	ctxt = ''
	for i in range(len(ptxt)):
		if ptxt[i] == '_':
			ctxt += '_'
			continue
		x = chr_to_num[ptxt[i]]
		y = chr_to_num[key[i]]
		ctxt += num_to_chr[(x + y) % 26]
	return ctxt

# ptxt = flag[5:-1]
# ctxt = encrypt(ptxt,key)
# pseudo_key = encrypt(key,key)

# print('Ciphertext:',ctxt)
# print('Pseudo-key:',pseudo_key)

flag = 'z_jjaoo_rljlhr_gauf_twv_shaqzb_ljtyut'
know_key = 'redpwwwnctf'
ptxt = decrypt(flag,know_key)

print('Plantext:',ptxt)
print('Pseudo-key:',know_key)