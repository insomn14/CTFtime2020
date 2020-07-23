def main(inpString):
    xorKey = 'S'
    length = len(inpString)

    for i in range(length):
        inpString = inpString[:i] + chr(ord(inpString[i]) ^ ord(xorKey)) + inpString[i+1:]

    return inpString

print(main('flag{fake_flag}'))
