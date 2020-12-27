def dec3(a1, a2):
    a1 = bytearray(a1)
    v4 = len(a1)
    for i in range(v4):
        if a1[i] > 47 and a1[i] <= 64:
            a1[i] -= a2
        i += 1
    return a1

def dec2(a1, a2):
    a1 = bytearray(a1)
    new = ''
    v4 = len(a1)
    for i in range(v4):
        new += chr(a1[(i-a2)%v4])
    return new

def dec1(a1, a2):
    a1 = bytearray(a1)
    i = 0
    while(i < len(a1)):
        if a1[i] > 96 and a1[i] <= 122:
            a1[i] = (a1[i] + 46 - a2) % 26 + 97
        if a1[i] > 64 and a1[i] <= 90:
            a1[i] = (a1[i] + 52 - a2) % 26 + 65
        i+=3
    return a1

mnt = input("Key : ") % 6 + 2
dec = raw_input("Cipher : ")
res = dec1(dec2(dec3(dec, mnt), mnt), mnt)
print "Plantext :",res
