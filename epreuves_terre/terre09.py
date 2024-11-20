import sys

arguments = sys.argv[1:]

for argument in arguments:
    if len(argument) < 1:
        print("erreur.")
        sys.exit()

number_str = sys.argv[1]

if not number_str.isdigit():
    print("erreur.")
    sys.exit()

number = int(number_str)

if number < 0:
    print("erreur.")
    sys.exit()

result = 0

while (result + 1) * (result + 1) <= number:
    result += 1

print(result)