import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
    print("erreur.")
    sys.exit()

argument = sys.argv[1]

if argument.isdigit():
    print("erreur.")
    sys.exit()

string_count = 0
for char in argument:
    string_count += 1

print(string_count)