#!/usr/bin/python
import md5

def main():
    find_hashd = '267530778aa6585019c98985eeda255f'
    mamber_list = ['bashninja', 'zestyfe', 's7a73farm', 'nullb0n3s', 'n30', 'ninjula', 'djjackalope', 'djtinehnimjeh', 'prestonpace', 'tinehnimjeh', 'missjackalopepatron']
    color_list = ['white', 'yellow', 'blue', 'red', 'green', 'black', 'brown', 'azure', 'ivory', 'teal', 'silver', 'purple', 'navy blue', 'peagreen', 'gray', 'orange', 'maroon', 'charcoal', 'aquamarine', 'coral', 'fuchsia', 'wheat', 'lime', 'crimson', 'khaki', 'pink', 'hotpink', 'magenta', 'olden', 'plum', 'olive', 'cyan']
    years_list = [str(years) for years in range(1600, 2021)]

    for name in mamber_list:
        for color in color_list:
            for years in years_list:
                hashd = md5.new()
                hashd.update('%s-%s-%s' % (color, years, name))
                if hashd.hexdigest() == find_hashd:
                    print('flag{%s-%s-%s}' % (color, years, name))
                    break

if __name__ == '__main__':
    main()
