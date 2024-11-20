import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
    print("erreur.")
    sys.exit()

number = sys.argv[1]

if not number.isdigit():
    print("erreur.")
    sys.exit()

number = int(number)

if number <= 1:
    print(f"Non, {number} n'est pas un nombre premier.")
    sys.exit()

if number > 1:
    for i in range(2, number):
        if (number % i) == 0:
            print(f"Non, {number} n'est pas un nombre premier.")
            sys.exit()
    else:
            print(f"Oui, {number} est un nombre premier.")