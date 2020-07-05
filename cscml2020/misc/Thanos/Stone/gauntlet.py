snap = b''
stones = ['power', 'space', 'reality', 'soul', 'time', 'mind']

for gem in stones:
    with open(gem, 'rb') as data:
        snap += data.read()
print(snap)
