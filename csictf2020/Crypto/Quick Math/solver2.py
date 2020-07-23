import gmpy
from Crypto.Util.number import long_to_bytes as ltb

N1 = 86812553978993
N2 = 81744303091421
N3 = 83695120256591
c1 = 8875674977048
c2 = 70744354709710
c3 = 29146719498409
e = 3

tA = c1 * (N2*N3) * gmpy.invert(N2*N3, N1)
tB = c2 * (N1*N3) * gmpy.invert(N1*N3, N2)
tC = c3 * (N1*N2) * gmpy.invert(N1*N2, N3)

c = (tA + tB + tC) % (N1*N2*N3)

m = gmpy.root(c,e)[0]
print(ltb(m))
	
