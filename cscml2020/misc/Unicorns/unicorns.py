#!/usr/bin/python3
import subprocess
from string import printable

def validate_input(inp):
    for c in inp:
        if c not in printable:
            return False
    return True

print("************************************************************")
print("***                        UNICORNS                      ***")
print("***                          ARE                         ***")
print("***                      M A G I C A L                   ***")
print("************************************************************")

print()
print("Enter your favorite unicorn's details:")

unicorn_color = input("Unicorn's color?\n")
unicorn_fur = input("Describe the texture of the unicorn's fur\n")
unicorn_hobby = input("What does your unicorn like to do?\n")

unicorn_color_len = len(unicorn_color)
unicorn_fur_len = len(unicorn_fur)
unicorn_hobby_len = len(unicorn_hobby)

unicorn_color = unicorn_color.upper()
unicorn_fur = unicorn_fur.upper()
unicorn_hobby = unicorn_hobby.upper()

if not all(map(validate_input, [unicorn_color, unicorn_fur, unicorn_hobby])):
    print("This is a program about unicorns! why are you doing this?!")
    exit(-1)

args = map(str, ("./analyze_unicorn", unicorn_color, unicorn_color_len, unicorn_fur, unicorn_fur_len, unicorn_hobby, unicorn_hobby_len))

popen = subprocess.Popen(args, stdout=subprocess.PIPE)
popen.wait()
output = popen.stdout.read()
print(output.decode("ascii"))


