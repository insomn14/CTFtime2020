print("\ntoast-clicker1\n")
s = [67, 83, 68, 120, 62, 109, 95, 90, 92, 112, 85, 73, 99, 82, 53, 99, 101, 92, 80, 89, 81, 104]
flag = ""
for i, c in enumerate(s):
	flag += chr(c+i)
print("FLAG : %s"%flag)

#----------------------------------------------------------------

print("\ntoast-clicker2\n")
import hashlib

from Crypto.Cipher.AES import MODE_ECB
from Cryptodome.Cipher import AES

KEY_PART1 = '742375c48a7'	# BuildConfig.java
key_part2 = 'da605b16'		# /resources/res/values/strings.xml
key_part3 = '49c9b7118e61'	# from nativ lib
key123 = '742375c48a70da605b1649c9b7118e61'
cipher = 'MwDxTPEvfSLms0PVdgxjYwgpgN8Y8Xj3Hrkw9pFkV6o='.decode('base64')

aes = AES.new(hashlib.sha1(key123).digest()[:16], MODE_ECB)
print(aes.decrypt(cipher))

#----------------------------------------------------------------

print("\ntoast-clicker3\n")
mapping = {
	"iiijj": 'a',
	"jjjii": 'b',
	"jijij": 'c',
	"jjijj": 'd',
	"jjjjj": 'e',
	"ijjjj": 'f',
	"jjjji": 'g',
	"iijii": 'h',
	"ijiji": 'i',
	"iiiji": 'j',
	"jjjij": 'k',
	"jijji": 'l',
	"ijiij": 'm',
	"iijji": 'n',
	"ijjij": 'o',
	"jiiji": 'p',
	"ijijj": 'q',
	"jijii": 'r',
	"iiiii": 's',
	"jjiij": 't',
	"ijjji": 'u',
	"jiiij": 'v',
	"iiiij": 'w',
	"iijij": 'x',
	"jjiji": 'y',
	"jijjj": 'z',
}

enc = ["ijiijiiijjjjjijijijiiijjijjjji","jjjiiiiijjjijijijjijiijji","jiijiiiijjiijjijijijiiijjjjjijjjjjjiiiii"]
flag = ""
tmp = ""
for en in enc:
	for ch in en:
		tmp += ch
		if len(tmp) == 5:
			flag += mapping[tmp]
			tmp = ""

print("FLAG : CTF{{{}}}".format(flag))
