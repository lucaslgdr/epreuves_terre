import sys

arguments = sys.argv[1:]

for argument in arguments:
    if len(arguments) != 3:
        print("erreur.")
        sys.exit()
    else:
        first_number = sys.argv[1]
        second_number = sys.argv[2]
        third_number = sys.argv[3]

if not argument.isdigit() or first_number == second_number == third_number:
    print("erreur.")
    sys.exit()

first_number = int(first_number)
second_number = int(second_number)
third_number = int(third_number)

if first_number == second_number or first_number == third_number or second_number == third_number:
    print("erreur.")
    sys.exit()

if second_number > first_number > third_number or third_number > first_number > second_number:
    print(first_number)
elif first_number > second_number > third_number or third_number > second_number > first_number:
    print(second_number)
elif first_number > third_number > second_number or second_number > third_number > first_number:
    print(third_number)