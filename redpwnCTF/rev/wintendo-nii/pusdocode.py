
com = 'Maro'
rsi = 'Cart50726E634D61726F43617274'
dil = 0

for bl in rsi:
	cl = 7
	while cl > 0:
		dil = (dil >> 1)
		r10b = (bl >> cl) & 1
		cl -= 1