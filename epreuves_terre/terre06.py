import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
    print("erreur.")
    sys.exit()

string = sys.argv[1]

if string.isdigit():
    print("erreur.")
    sys.exit()

reversed_string = ""
for char in string:
    reversed_string = char + reversed_string

print(reversed_string)