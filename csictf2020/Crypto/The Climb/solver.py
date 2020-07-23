#!/usr/bin/python3
from itertools import product
from string import ascii_lowercase as lc

def txtconv(text):
	tmx = []
	for i in text:
		tmp = ord(i) - 97
		tmx.append(tmp)
	return tmx


def mul(tmx, ln):
	rmx = [0 for _ in range(ln)]
	for i in range(ln):
		for j in range(ln):
			rmx[i] = rmx[i] + kmx[i][j] * tmx[j]
		rmx[i] = rmx[i] % 26
	return rmx


def res(rmx, ln):
	r = ''
	for i in rmx:
		r += chr(i+97)
	return r


flag = ['lrz', 'lhh', 'omb', 'gic', 'hae']
kmx = [[6, 24, 1], [13, 16, 10], [20, 17, 15]]
get = ''
cnt = 0
while len(get) != len(''.join(flag)):
	for ch in product(lc, lc, lc):
		tmp = ''.join(ch)
		fin = res(mul(txtconv(tmp), 3), 3)
		if all(i == j for i,j in zip(fin,flag[cnt])):
			cnt += 1
			get += tmp
			print('Found {}'.format(get))
			break