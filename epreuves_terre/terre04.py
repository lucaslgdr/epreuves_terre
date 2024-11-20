import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
    print("Tu ne me la mettras pas à l'envers.")
    sys.exit()

argument = sys.argv[1]

if argument.isdigit():
    number = int(argument)
else:
    print("Tu ne me la mettras pas a l'envers.")
    sys.exit()

if number % 2 == 0:
    print("Pair.")
else:
    print("Impair.")