#!/usr/bin/python3
import subprocess
from string import printable

comp = open('output.txt', 'r').read().strip()[1:-1].split(', ')

flag = 'rgbCTF{'
while len(flag) != len(comp):
	for ch in printable:
		argv = flag + ch
		args = map(str, ('./itJX.so', argv))

		popen = subprocess.Popen(args, stdout=subprocess.PIPE)
		popen.wait()
		output = popen.stdout.read().decode('ascii')[1:-2].split(', ')
		if all(i==j for i,j in zip(output, comp)):
			flag += ch
			# print(f'Found : {flag}') # debug output
			break
print(f'Found : {flag}')