# [Crypto] Solution

***

## Gross 120pts

```
Cipher: OQWKWPUVMYTIUSSTHHPI

Keep this: 12345 , will help you. Flag format: noob{FLAG}

Author: D3v1LaL
```

In CTF competitions the title of the challenge sometimes can be a clue. For example in this challenge, I thought that the word 'Gross' was a play on words from 'Grons' so I concluded it might be 'Gronsfeld Cipher'. The conclusion I got after reading the [pycipher](https://pycipher.readthedocs.io/en/master/\#id16) documentation.

```
>>> import pyciphet
>>>
>>> msg = pycipher.Gronsfeld([1,2,3,4,5]).decipher('OQWKWPUVMYTIUSSTHHPI')
>>> msg
'NOTGROSSITSGRONSFELD'
```

FLAG : `noob{NOTGROSSITSGRONSFELD}`

***

## Aar\_Ess\_Ae 2.0 200pts

```
Optimus Prime Loves The Title Of This Song: https://www.youtube.com/watch?v=wyx6JDQCslE

Author: D3v1LaL
```

We were given an aresae2.txt file that contained
```
n: 1209143407476550975641959824312993703149920344437422193042293131572745298662696284279928622412441255652391493241414170537319784298367821654726781089600780498369402167443363862621886943970468819656731959468058528787895569936536904387979815183897568006750131879851263753496120098205966442010445601534305483783759226510120860633770814540166419495817666312474484061885435295870436055727722073738662516644186716532891328742452198364825809508602208516407566578212780807
e: 65537
c: 479864533376761605695501447173868480555428955121197237667644363164782871896916177280454277070395501072881821206028710238061428135752902868021510351013602427444705377461961807606024656743172785917677779391848195684330103645049456693618142623342949445393135435605296850775153054696353591431012573391751673267024658145416936335505273041995697052197680305689264142043959382559774510439925577487721780439642813074520685265074584526487330950173513520723457640547997316 
```

I use [RsaCtfTool](https://github.com/Ganapati/RsaCtfTool) to help me get a private key. After that we can create simple script to decrypt value of c
<code>

	from Crypto.Util.number import long_to_bytes
	from Crypto.PublicKey import RSA

	c = 479864533376761605695501447173868480555428955121197237667644363164782871896916177280454277070395501072881821206028710238061428135752902868021510351013602427444705377461961807606024656743172785917677779391848195684330103645049456693618142623342949445393135435605296850775153054696353591431012573391751673267024658145416936335505273041995697052197680305689264142043959382559774510439925577487721780439642813074520685265074584526487330950173513520723457640547997316
	f = open('keypair.pem', 'r').read()
	key = RSA.importKey(f)
	m = long_to_bytes(pow(c, key.d, key.n))
	with open('flag.txt', 'w') as w:
			w.write(str(m))
			w.close()
	print(m)

</code>

FLAG : `noob{Primes_Can_B3_Saxy_T00}`

***

## CrackMeh 250pts

```
3lli0t found a diary from Evil Corp. He have to get into the system, but can't as he have a hash of a password and no plaintext. Help him to get into system.

flag format: noob{plaintext}

hash: 4ee805f9397a1d584ef9be9d2a4f8f20

Author: D3v1LaL
```

We were given an diary.txt file that contained
```
_________________________
|                       |
|                       |
|                       |
|         Alice         |
|        January        |
|         1994          |
|         USA           |
|          25           |
|       Security        |
|                       |
|                       |
|_______________________|
```

To solve this challenge, we can use diary.txt as information, maybe the hash contains some of these words.

<code>

	from itertools import permutations
	import hashlib

	def checked(inc, data):
		for data in permutations(data, inc):
			temp = bytes(''.join((data)), 'utf-8')
			m = hashlib.md5()
			m.update(temp)
			result = m.hexdigest()
			if result == hashed:
				print(f'FOUND : {result} -> {temp}')
				return True
		return False

	hashed = '4ee805f9397a1d584ef9be9d2a4f8f20'
	data = ['Alice', 'January', '1994', 'USA', '25', 'Security']
	for cnt in range(1, len(data)+1):
		if checked(cnt, data):
			exit()

</code>

FLAG : `noob{AliceSecurity1994}`

***

## Frequency 250pts

```
Elliot captured something, while noob called his friend

Flag format: noob{FLAG}

Author: D3v1LaL
```

in this challenge we were given Cipher.txt file
```
1209-770 1209-770 1477-697 1477-697 1336-770 1336-770 1336-770 1336-770 1336-770 1336-770 1477-770 1477-770 1477-770 1477-697 1336-852 1477-770 1477-697 1477-697 1477-697
```

As I mentioned earlier, the title of the challenge is usually a hint. The following challenges are [DTMF](https://en.wikipedia.org/wiki/Dual-tone_multi-frequency_signaling) keypad frequencies.

After decoding the signal we will get a number `44335555566386333`, 
replace the numbers you have obtained with the letter at each press of the T9 keyboard.
`HELLODTMF`

FLAG : `noob{HELLODTMF}`