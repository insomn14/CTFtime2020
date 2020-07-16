from itertools import permutations
from string import printable
import hashlib 

rainbows = open('rainbows.txt', 'r').read().split('\n')

plaintext = ''
while len(plaintext) != len(rainbows):
	for i in range(1,3):
		for str2hash in permutations(printable, i):
			# print('Trying : {}'.format(''.join(str2hash)))
			result = hashlib.md5(''.join(str2hash).encode()) 
			if result.hexdigest() == rainbows[len(plaintext)]:
				plaintext += ''.join(str2hash)
				print('Found : {}'.format(plaintext))
				break

print('Result : {}'.format(plaintext)) 