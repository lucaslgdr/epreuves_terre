import sys

arguments = sys.argv[1:]

if len(arguments) != 2:
    print("erreur.")
    sys.exit()

number = sys.argv[1]
exposant = sys.argv[2]

if not number.isdigit() and not exposant.isdigit():
    print("erreur.")
    sys.exit()

number = int(number)
exposant = int(exposant)

if exposant < 0:
    print("erreur.")
    sys.exit()

result = 1
for i in range(exposant):
    result *= number

print(result)