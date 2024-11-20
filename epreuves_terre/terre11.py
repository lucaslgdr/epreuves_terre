import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
    print("erreur.")
    sys.exit()

heure_24 = sys.argv[1]

if heure_24.isdigit():
    print("erreur.")
    sys.exit()

heure_24 = str(heure_24)

heure = heure_24[0:2]
minutes = heure_24[3:5]
minutes = int(minutes)
heure = int(heure)
heure_12 = heure - 12

if heure > 24:
    print("erreur.")
    sys.exit()

if minutes > 59:
    print("erreur.")
    sys.exit()

if heure < 12:
    print(heure,":", minutes, "AM")
elif heure_24 == "00:00":
    print("12 : 00 AM")
else:
    heure_12 = str(heure_12)
    print(heure_12,":", minutes,"PM")