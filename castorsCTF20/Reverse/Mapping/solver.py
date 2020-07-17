import string


firstString  = 'xzstorsXWA{zyxjklmdefghinopqrstuvwcba56701234895_ZYX}'
secondString = 'castorsCTF{abcdefghijklmnopqrstuvwxyz01234567890_ABC}'



string = 'xzstorsXWA{ib_4r1n2h1465n_41yh0_62_y0440r_4d1n_b5ur2}'

print("Original string:", string)

translation = string.maketrans(firstString, secondString)

# translate string
print("Translate string:", string.translate(translation))
