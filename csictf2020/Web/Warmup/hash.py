from hashlib import sha1

i = 0
while True:
    pt = '0e%d' % i
    s = sha1()
    s.update(pt)
    h = s.hexdigest()

    if h.startswith('0e'):
        if h[2:].isdigit():
            print(pt, h)
            break
    i += 1
