from string import printable


def solve(p1):
    p1 += 2
    if p1 > 96 and p1 <= 122:
        p1 = (p1 - 87) % 26 + 97
    return p1

enc = [0x64, 0x35, 0x68, 0x35, 0x64, 0x37, 0x33, 0x7a, 0x38, 0x6b, 0x33, 0x37, 0x6b, 0x72, 0x67, 0x7a]

dec = ''
while len(dec) < len(enc):
    for ch in printable:
        if solve(ord(ch)) == enc[len(dec)]:
            dec += ch
            print(f"Found : {dec}")


