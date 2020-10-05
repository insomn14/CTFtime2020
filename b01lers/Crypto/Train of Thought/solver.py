import Levenshtein as L
from itertools import permutations
from string import ascii_lowercase as lw

f = open('trainofthought.txt').read().strip().split(' ')

idx = []
for i in range(len(f)-1):
	idx.append(L.distance(f[i], f[(i+1)%len(f)]))

print(idx)

lw = '\x00' + lw
flag = ''.join(lw[j%len(lw)] for j in idx)
print(flag)
