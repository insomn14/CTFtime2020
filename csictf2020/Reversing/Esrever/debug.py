import random

# TODO: Remember to remove real flag before deploying
flag = 'csictf{esreverisjustreverseinreverseright}'
key = 'insovietrussiapikachucatchesyou'

def enc1(text):
    r = random.randint(1,25)
    return bytes.fromhex(''.join([hex(((ord(i) - ord('a') - r) % 26) + ord('a'))[2:] for i in text])).decode('ascii')
    
def enc2(text, key):
    k = [key[i % len(key)] for i in range(len(text))]
    return ''.join([chr(ord(text[i]) ^ ord(k[i]) + ord('a')) for i in range(len(text))])

def enc3(text):
    mapping = [28, 33, 6, 17, 7, 41, 27, 29, 31, 30, 39, 21, 34, 15, 3, 5, 13, 10, 19, 38, 40, 14, 26, 25, 32, 0, 36, 8, 18, 4, 1, 11, 24, 2, 37, 20, 23, 35, 22, 12, 16, 9]

    temp = [None]*len(text)
    for i in range(len(text)):
        temp[mapping[i]] = text[i]
    
    return ''.join(temp)

def enc4(text):
    mapping = [23, 9, 5, 6, 22, 28, 25, 30, 15, 8, 16, 19, 24, 11, 10, 7, 2, 14, 18, 1, 29, 21, 12, 4, 20, 0, 26, 13, 17, 3, 27]

    temp = [None]*len(text)
    for i in range(len(text)):
        temp[i] = text[mapping[i]]
    
    return ''.join(temp)

encryptedText = enc1(flag)
print(encryptedText)
encryptedKey = enc1(key)
for i in range(random.randint(1,100)):
    encryptedText = enc1(encryptedText)
    encryptedKey = enc1(key)

print('Encrypted Key = ' + enc4(enc4(encryptedKey)))
print('Encrypted Text = ' + enc3(enc3(enc2(enc1(encryptedText), key))))


# ---------------- SOLUTION --------------
# def dec3(text):
#     mapping = [25, 30, 33, 14, 29, 15, 2, 4, 27, 41, 17, 31, 39, 16, 21, 13, 40, 3, 28, 18, 35, 11, 38, 36, 32, 23, 22, 6, 0, 7, 9, 8, 24, 1, 12, 37, 26, 34, 19, 10, 20, 5]
#     temp = [None]*len(text)
#     for i in range(len(text)):
#         temp[mapping[i]] = text[i]
#     return ''.join(temp)

# def dec4(text):
#     mapping = [25, 19, 16, 29, 23, 2, 3, 15, 9, 1, 14, 13, 22, 27, 17, 8, 10, 28, 18, 11, 24, 21, 4, 0, 12, 6, 26, 30, 5, 3, 7]
#     temp = [None]*len(text)
#     for i in range(len(text)):
#         temp[i] = text[mapping[i]]
#     return ''.join(temp)

# ENCRYPTED KEY :
# encryptedKey = 'ieluvnvfgvfahuxhvfphbppnbgrfcrn'
# encryptedKey = enc4(enc4(encryptedKey)) # 'vafuivrgehffvncvxnpuhpngpurflrh'
#
# >>> enc1 = lambda text, r=random.randint(1,25): bytes.fromhex(''.join([hex(((ord(i) - ord('a') - r) % 26) + ord('a'))[2:] for i in text])).decode('ascii')
# >>> text = 'vafuivrgehffvncvxnpuhpngpurflrh'
# >>> tampung = []
# >>> for i in range(1,25):
# ...     tmp = enc1(text, i)
# ...     for j in range(1,25):
# ...             tmp1 = enc1(tmp, j)
# ...             if tmp1 not in tampung:
# ...                     tampung.append(tmp1)
#
# print('Encrypted Key = ' + enc4(enc4(encryptedKey)))
# result -> encryptedKey -> 'in shviet russia pikachu catches yeu' : (1, 'uzethuqfdgeeumbuwmotgomfotqekqg', 12, 'inshvietrussiapikachucatchesyeu')
# 'in soviet russia pikachu catches you' => 'insovietrussiapikachucatchesyou'
#
# TEST OuR OwN KEY
# >>> enc1(enc1(text_ori, 12),1)
# 'vafbivrgehffvncvxnpuhpngpurflbh'


# ENCRYPTED FLAG :
# EncryptedText = "»·­ª»£µ±¬¥¼±ºµ±¿·£¦­´¯ª¨¥«¥¦«´¸¦¡¸¢²§¤¦¦¹¨"
# EncryptedText -> enc3(enc3(EncryptedText)) => '¦­¦¼´¥¬»±·º±¤££¨¿¦¦ª·ª§»¥«¨¦­±¸¯¡µ²¹«´¥¢µ¸'
#
# EncryptedText = '¦­¦¼´¥¬»±·º±¤££¨¿¦¦ª·ª§»¥«¨¦­±¸¯¡µ²¹«´¥¢µ¸'
# EncryptedText -> enc2(EncryptedText, key) => 'lbrlcojnbanenarbsdbcanenabnrwanenabnarpqcl'
#
#
# >>> tumpang = []
# data = 'lbrlcojnbanenarbsdbcanenabnrwanenabnarpqcl'
# >>> for i in range(1,25):
# ...     tmp1 = enc1(data, i)
# ...     for j in range(1,25):
# ...             tmp2 = enc1(tmp1, j)
# ...             for k in range(1, 25):
# ...                     tmp3 = enc1(tmp2, k)
# ...                     if tmp3 not in tampung:
# ...                             i, tmp1, j, tmp2, k, tmp3
# ...                             tampung.append(tmp3)
#
# (1, 'kaqkbnimazmdmzqarcabzmdmzamqvzmdmzamzqopbk', 1, 'jzpjamhlzylclypzqbzaylclyzlpuylclyzlypnoaj', 7, 'csictfaesreverisjustreverseinreverserightc')
# csictfaesreverisjustreverseinreverserightc
# csictf{esreverisjustreverseinreverseright}
