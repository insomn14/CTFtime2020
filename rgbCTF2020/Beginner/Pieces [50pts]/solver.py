#  text.charAt(i) % 2 == 0 ? "|" : "/";
# "9|2/9/:|4/7|8|4/2/1/2/9/"

ft = {True:'|', False:'/'}
con = '|//|/||/////'
res = '929:47842129'

plaintext = ''
while len(plaintext) != len(res):
	for i, c in enumerate(res):
		rec = ord(c) * 2
		if ft[rec % 2 == 0] == con[i]:
			plaintext += chr(rec)
		else:
			plaintext += chr(rec+1)
print(plaintext)
