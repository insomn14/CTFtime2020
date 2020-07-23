from string import printable

usr = '23ab3315dfa57aeac49011e93ae787c65576538098b56b4dc2b789cc23fea833'.decode('hex')
pwd = '23ab3315dfa57aeac49011e93ae787c66a9677086381d4176b12ac298aafe2b3'.decode('hex')

assert usr[:16] == pwd[:16]

usr_inp = 'user:c?i'
pwd_inp = 'pass:c?f'

iv = usr[:16]
usr_en = usr[16:]
pwd_en = pwd[16:]

xor = lambda x,y : ''.join([ chr( ord(i) ^ ord(j) ) for i, j in zip(x,y)])

know = usr_inp
while len(know) != len(usr_en):
    for ch in printable:
        tmp = know + ch
        res = xor(tmp, iv)
        print(usr_en)
        if all([i==j for i,j in zip(res, usr_en)]):
            know += ch
            print(know)
            break
