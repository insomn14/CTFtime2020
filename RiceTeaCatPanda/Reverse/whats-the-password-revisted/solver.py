from z3 import *

def main():
	s = Solver()

	comp = [58,49,82,48,52,54,82,48,51,92,58,81,115,48,53,69,92,49,90,52]

	inp = [BitVec('a%d'%i,32) for i in range(len(comp))]

	for i in range(len(inp)):
		s.add(comp[i]==((inp[i]^50)+1)^50)

	if s.check() == sat:
		raw = s.model()
		res = [chr(int(str(raw[inp[i]]))) for i in range(len(inp))]
	        print ''.join(res)
        else:
        	print('Gaga!..')

main()