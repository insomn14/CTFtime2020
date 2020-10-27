import Levenshtein as L
import string


f = open("trainofthought.txt", "r").read().strip().split(' ')
flag = ''
for i in range(len(f)-1):
	dist = L.distance(f[i], f[i+1])
	chrs = string.ascii_lowercase[dist-1]
	flag += chrs		
print(flag)
