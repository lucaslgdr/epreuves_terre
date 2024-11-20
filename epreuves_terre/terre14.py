import sys

if len(sys.argv) <= 1:
    print("erreur.")
    sys.exit()

numbers = sys.argv[1:]

for arguments in numbers:
    if not arguments.isdigit():
        print("erreur.")
        sys.exit()

is_sorted = True

for i in range(1, len(numbers)):
    if numbers[i] < numbers[i -1]:
        is_sorted = False
        break

if is_sorted:
    print("Triée !")
else:
    print("Pas triée !")