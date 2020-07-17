from pwn import *
from string import printable

host, port = 'localhost', 8080

def send_recv(data):
	r.sendlineafter('choice: ', '1')
	r.sendlineafter('> ', data)
	r.recvuntil('\n')
	r.recvuntil('\n')
	s = r.recvuntil('\n').replace('\n', '')
	# log.info('DATA : {}'.format(s))
	return s

def test():
	print r.recvline()
	for i in printable:
		cek = send_recv('A'*48+i)
		print('DATA {} : {}'.format(i,cek))
		r.recvuntil('Your ')
	r.interactive()

# def main():
# 	flag = ""

# 	for x in range(48, 1, -1):
# 		init = 'A' * (x - 1)
# 		print init
# 		cipher_init = send_recv(init)
# 		print('DATA : {}'.format(cipher_init))
# 		for y in printable:
# 			guess = 'A' * (x - 1) + flag + y
# 			cipher_guess = send_recv(guess)
# 			print('DATA : {}'.format(cipher_guess))
# 			if cipher_init[:48] == cipher_guess[:48]:
# 				flag += y
# 				print("Found : {}".format(flag))
# 				break



if __name__ == '__main__':
	r = remote(host, port)
	main()
	# test()
