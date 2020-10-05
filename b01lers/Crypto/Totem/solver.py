import pycipher
from base64 import b64decode
from pwn import *

mapping = {
	'AAAAA':'a',
	'AAAAB':'b',
	'AAABA':'c',
	'AAABB':'d',
	'AABAA':'e',
	'AABAB':'f',
	'AABBA':'g',
	'AABBB':'h',
	'ABAAA':'i',
	'ABAAB':'j',
	'ABABA':'k',
	'ABABB':'l',
	'ABBAA':'m',
	'ABBAB':'n',
	'ABBBA':'o',
	'ABBBB':'p',
	'BAAAA':'q',
	'BAAAB':'r',
	'BAABA':'s',
	'BAABB':'t',
	'BABAA':'u',
	'BABAB':'v',
	'BABBA':'w',
	'BABBB':'x',
	'BBAAA':'y',
	'BBAAB':'z'
}


Atbash = lambda cip: pycipher.Atbash().decipher(cip).lower()
Rot13 = lambda cip: pycipher.Rot13().decipher(cip).lower()
Base64 = lambda cip: b64decode(cip).decode('utf-8')
bacon = lambda cip: ''.join(mapping[cip[i:i+5]] for i in range(0, len(cip), 5))


con = remote('chal.ctf.b01lers.com', 2008)

for cnt in range(1000):
	log.info(f'Count: {cnt+1}')

	con.recvuntil('Method: ')
	Method = con.recvuntil('\n').decode('utf-8').strip()

	con.recvuntil('Ciphertext: ')
	Ciphertext = con.recvuntil('\n').decode('utf-8').strip()
	log.info(f'Ciphertext: {Ciphertext}')

	if Method == 'atbash':
		text = Atbash(Ciphertext)
	elif Method == 'rot13':
		text = Rot13(Ciphertext)
	elif Method == 'Base64':
		text = Base64(Ciphertext)
	elif Method == 'bacon':
		text = bacon(Ciphertext)
	log.info(f'Input : {text}')
	con.sendlineafter('Input: ', text)

print(con.recv())