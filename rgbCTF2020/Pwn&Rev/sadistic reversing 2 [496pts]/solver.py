#!/usr/bin/python3
import subprocess
from string import printable
from itertools import product

def exec_args(a1):
	# execute binary file with args
	# ex: ./itwk.so <argv>
	argv = ''.join(a1)
	# print(f'Trying : {argv}') # debug output
	args = map(str, ('./itwk.so', argv))
	popen = subprocess.Popen(args, stdout=subprocess.PIPE)
	popen.wait()
	output = popen.stdout.read().decode('ascii')[1:-2].split(', ')
	return output


def main():
	comp = open('output.txt', 'r').read().strip()[1:-1].split(', ')
	
	arg = ['*' for _ in range(len(comp))]
	flag = ['*' for _ in range(len(comp))]
	find, cnt = 0, 0
	while '*' in arg:
		idx = 0
		for ch in product(printable):
			arg[cnt] = ''.join(ch)
			output = exec_args(arg)
			
			if output[find] == comp[find]:
				arg[cnt]  = ''.join(ch)
				flag = ''.join(arg)
				print(f'Found : {"".join(arg)}')
				cnt += 1
				find += 1
				if cnt == len(comp):
					cnt = 0
				break

			# update list(arg)
			if idx == 99:
				arg = [i for i in flag]
				cnt += 1
				break
			idx += 1

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as err:
		print(err)
