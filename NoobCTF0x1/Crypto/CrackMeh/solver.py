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
