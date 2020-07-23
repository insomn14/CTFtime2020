flag_enc = '¤Ä°¤ÆªÔ\x86$\xa04\x9cÌ`H\x9c¬>¼f\x9c¦@HH\xa0\x84¨\x9a\x9a¢vÐØ'

flag_dec = ''

for i in list(flag_enc):
    flag_dec += chr((ord(i) + len(flag_enc)) // 2)

print(flag_dec)
