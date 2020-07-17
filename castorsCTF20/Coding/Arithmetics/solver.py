from pwn import *
from string import digits
from word2number import w2n

mul = lambda x, y : str(x * y)
div = lambda x, y : str(x // y)
add = lambda x, y : str(x + y)
sub = lambda x, y : str(x - y)
cek = lambda x: w2n.word_to_num(x) 

host, port = 'chals20.cybercastors.com', 14429

r = remote(host, port)

print r.recvuntil('ready.\n')
r.sendline('')

# leak = r.recvuntil('?').split(' ')
# log.info('LEAK : {}'.format(leak))
# op = str(leak[-3])
# num1 = str(leak[-4])
# num2 = str(leak[-2])
# log.info('{} {} {} '.format(num1, op, num2))
# 
# if num1 not in [i for i in digits]:
# 	num1 = cek(num1)
# if num2 not in [i for i in digits]:
# 	num2 = cek(num2)
# if op == '*' or 'mul' in op:
# 	r.sendline(mul(int(num1), int(num2)))
# elif op == '/' or op == '//' or 'div' in op:
# 	r.sendline(div(int(num1), int(num2)))
# elif op == '+' or 'add' in op or 'plus' in op:
# 	r.sendline(add(int(num1), int(num2)))
# elif op == '-' or 'sub' in op or 'minus' in op:
# 	r.sendline(sub(int(num1), int(num2)))

cnt = 0
while True:
	r.recvuntil('\n')
	print r.recvline()
	leak = r.recvuntil('?').split(' ')
	log.info('{} LEAK : {}'.format(cnt, leak))

	op = str(leak[-3])
	num1 = str(leak[-4])
	num2 = str(leak[-2])
	log.info('{} {} {} '.format(num1, op, num2))

	if num1 not in [i for i in digits]:
		num1 = cek(num1)
	if num2 not in [i for i in digits]:
		num2 = cek(num2)
	if op == '*' or 'mul' in op:
		r.sendline(mul(int(num1), int(num2)))
	elif op == '/' or op == '//' or 'div' in op:
		r.sendline(div(int(num1), int(num2)))
	elif op == '+' or 'add' in op or 'plus' in op:
		r.sendline(add(int(num1), int(num2)))
	elif op == '-' or 'sub' in op or 'minus' in op:
		r.sendline(sub(int(num1), int(num2)))

	cnt += 1
	print cnt

r.interactive()
