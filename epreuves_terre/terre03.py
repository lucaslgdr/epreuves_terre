import sys

argument = sys.argv[1]
ascii_letter = ord(argument[0])

for ascii_letter in range(ascii_letter,123):
    print(chr(ascii_letter), end="")