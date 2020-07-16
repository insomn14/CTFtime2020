#!/usr/bin/python3
import subprocess
from string import printable

comp = open('cipher', 'r').read().strip()

flag = ''
while len(flag) != len(comp):
	for ch in printable:
		argv = flag + ch
		args = map(str, ('./lich', argv))

		popen = subprocess.Popen(args, stdout=subprocess.PIPE)
		popen.wait()
		output = popen.stdout.read().decode('utf-8').replace('\n', '')
		if all(x == y for x, y in zip(output, comp)):
			flag += ch
			print(f'Found : {flag}')
			break
print(flag)

with open('input.txt', 'w') as out:
	out.write(flag)
	out.close()