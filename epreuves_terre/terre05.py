import sys

arguments = sys.argv[1:]

if len(arguments) != 2:
    print("erreur.")
    sys.exit()

dividend = sys.argv[1]
divisor = sys.argv[2]

if not dividend.isdigit() and not divisor.isdigit():
    print("erreur.")
    sys.exit()

dividend = int(dividend)
divisor = int(divisor)

if dividend < divisor:
    print("erreur.")
    sys.exit()

if divisor == 0:
    print("erreur.")
    sys.exit()

résultat = dividend / divisor
print(f"résultat: {résultat}".split(".")[0])
reste = dividend % divisor
print(f"reste: {reste}".split(".")[0])