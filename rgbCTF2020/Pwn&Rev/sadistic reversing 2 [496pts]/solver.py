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
	# comp = ['117', '148', '123', '5', '54', '9', '61', '234', '45', '4', '2', '40', '88', '111', '65', '65', '46', '23', '114', '110', '102', '148', '136', '123', '30', '5', '214', '231', '225', '255', '239', '138', '211', '208', '250', '232', '178', '187', '171', '242', '255', '30', '39', '19', '64', '17', '40', '29', '13', '27']
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