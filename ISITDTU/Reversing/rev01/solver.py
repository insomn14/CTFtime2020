from itertools import permutations
from string import printable

CMP = list("KV3c09VQfFVdpN2afdVYy12XVB3XJ91VpNHafl1b19FShZXZfZUdu9FUsFWep52Zfl0UJRFRUV1XDRlR")
ABC = list("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/")

try:
	n, flag = 0, ''
	for c in permutations(printable, 6):
		inp = [ord(i) for i in c]
		for i in range(0, len(inp), 3):
			v9 = inp[i + 2]
			v3 = (v9 << 8) | inp[i + 1]
			v4 = (v3 << 8) | inp[i]
			if ABC[(v4 >> 18) & 0x3F] == CMP[n + 3] and ABC[(v4 >> 12) & 0x3F] == CMP[n + 2]:
				if ABC[(v4 >> 6) & 0x3F] == CMP[n + 1] and ABC[v4 & 0x3F] == CMP[n]:
					flag += "".join(c)[-3:]
					print(f'FOUND : {flag}')
					n += 4
except Exception:
	pass