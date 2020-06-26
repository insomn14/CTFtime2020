#!/usr/bin/python3

import _thread
from numba import njit
from itertools import permutations
from string import ascii_letters, ascii_lowercase, digits, printable


xor = lambda x: [i^18 for i in x]
conv_int = lambda x : [ord(i) for i in x]
conv_chr = lambda x : ''.join([chr(i) for i in x])

# @njit
def aneh(a1, a2, a3):
	gg = []
	while a2 != a3:
		v4 = (a1[a2 - 1] >> 1) + 2 * (a1[a2])
		gg.append((v4 >> (v4 >> 7)) - 1)
		a2 += 1
	return gg

# @njit
def main(msg, f, s1, s2):
	for passwd in permutations(strings, f):
		tmp = conv_chr(aneh(conv_int(passwd), 1, f))
		print(tmp)
		if tmp == enc[s1:s2]:
			print(msg, ''.join(passwd), tmp)


if __name__ == '__main__':
	strings = ascii_letters + digits + '_'
	enc = 'te@B}efFk~{^Ixv@}y\\BC4'

	try:
		_thread.start_new_thread( main, ('Frist :', 5, 0, 4, ) )
		_thread.start_new_thread( main, ('Second :', 5, 4, 8, ) )
		_thread.start_new_thread( main, ('Thrid :', 5, 8, 12, ) )
		_thread.start_new_thread( main, ('Four :', 5, 12, 16, ) )
		_thread.start_new_thread( main, ('Five :', 5, 16, 20, ) )
		# _thread.start_new_thread( main, ('Six :',4, 15, 18, ) )
		# _thread.start_new_thread( main, ('Seven :',4, 18, 22, ) )
	except KeyboardInterrupt as err:
		print(err)
	except:
		print ("Error: unable to start thread")

while 1:
   pass
