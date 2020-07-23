def main(text, counter):
    ret_text = ''
    for i in list(text):
        counter = text.count(i)
        ret_text +=  chr((2 * ord(i)) - len(text))
    return ret_text

print(main(text, ''))
