from pwn import *
from string import digits
from word2number import w2n

mul = lambda x, y : str(x * y)
div = lambda x, y : str(x // y)
add = lambda x, y : str(x + y)
sub = lambda x, y : str(x - y)
cek = lambda x: w2n.word_to_num(x) 

op_div = ['/', '//', 'divided-by']
op_add = ['+', 'add', 'plus']
op_mul = ['*', 'multiplied-by']
op_min = ['-', 'sub', 'minus']

host, port = 'chals20.cybercastors.com', 14429
r = remote(host, port)
r.sendline('')
r.recvuntil('ready.\n')
cnt = 1
while cnt < 101:
	# leak = r.recvuntil(' ?\n').split(' ')
	leak = r.recvuntil('\n').split(' ')
	log.info('{} LEAK : {}'.format(cnt, leak))

	op = str(leak[-3])
	num1 = str(leak[-4])
	num2 = str(leak[-2])
	log.info('{} {} {} '.format(num1, op, num2))

	if num1 not in [i for i in digits]:
		num1 = cek(num1)
	if num2 not in [i for i in digits]:
		num2 = cek(num2)
	if op in op_mul:
		r.sendline(mul(int(num1), int(num2)))
	elif op in op_div:
		r.sendline(div(int(num1), int(num2)))
	elif op in op_add:
		r.sendline(add(int(num1), int(num2)))
	elif op in op_min:
		r.sendline(sub(int(num1), int(num2)))

	print r.recvline()

	cnt += 1

print r.recv()
r.interactive()
