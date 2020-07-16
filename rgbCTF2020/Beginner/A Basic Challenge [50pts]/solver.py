from base64 import b64decode

data = open('basic_chall.txt', 'r').read().strip().split(' ')

# binary to ascii
tmp1 = ''
for biny in data:
	tmp1 += chr(int(biny, 2))
# print(tmp1)

# hex to ascii
tmp2 = ''
for hx in tmp1.split(' '):
	tmp2 += chr(int(hx, 16))
# print(tmp2)

# decode base64
tmp3 = b64decode(tmp2)
# print(tmp3)

# ocatal to ascii
res = ''
for oc in tmp3.split(' '):
	res += chr(int('0'+oc, 8))
print(res)
