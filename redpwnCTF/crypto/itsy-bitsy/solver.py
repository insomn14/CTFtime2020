#!/usr/bin/env python3

from Crypto.Random.random import randint
from string import ascii_letters

conv = lambda x: "".join([chr(int(binary, 2)) for binary in x.split(" ")]) # convert binary to ascii
splits = lambda x: [x[i*7:(i*7)+7] for i in range(len(x)//7)]

def str_to_bits(s):
	bit_str = ''
	for c in s:
		i = ord(c)
		bit_str += bin(i)[2:]
	return bit_str

def bit_str_xor(bit_str_1, bit_str_2):
	xor_res = ''
	for i in range(len(bit_str_1)):
		bit_1 = bit_str_1[i]
		bit_2 = bit_str_2[i]
		xor_res += str(int(bit_1) ^ int(bit_2))
	return xor_res

# key = 'UW]_uw}\x7f'
strings = ''.join(chr(i) for i in range(2**6,2**7))
cp = '0111111010111000101010001101001100001001000110001001011100101010111101011001000011010011000010111001101000110001001001101011010001110001111100010000000100011111101100000011100010101000010000101000011111101111010010010010011001111010111111001001100011100101111011101000011010100110000111001011000111010'
flags = ascii_letters + '_}{'
flag = ''.join(conv(i) for i in splits(cp))

cnt = 0
while cnt < len(flag)-1:
	for ch in strings:
		tmp = ch ^ 