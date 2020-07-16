f = open('fix.java', 'rb').read().strip()
d = open('DifferenceTest.java', 'rb').read().strip()

assert len(f) == len(d)

w, g = '', ''
for x, y in zip(f, d):
	if x != y:
		w += chr(y)
		g += chr(x)

assert len(w) == len(g)

sub = lambda x, y : ''.join(chr(ord(i)-ord(j)) for i, j in zip(w,g))
print(sub(w,g))
# 'rgbCTF{tr1pl3_m34n1ng}'