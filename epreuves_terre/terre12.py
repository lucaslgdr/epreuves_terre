import sys

arguments = sys.argv[1:]

if len(arguments) != 1:
    print("erreur.")
    sys.exit()

heure_12 = sys.argv[1]

if heure_12.isdigit():
    print("erreur.")
    sys.exit()

heure_12 = str(heure_12)

heure = heure_12[0:2]
minutes = heure_12[3:5]
minutes = int(minutes)
heure = int(heure)
heure_24 = heure + 12

if heure < 12 and heure_12[5] == "A" or "a":
    heure_12 = str(heure_12)
    print(heure_12[0:2],":", minutes)
    sys.exit()

if heure > 12:
    print("erreur.")
    sys.exit()

if minutes > 59:
    print("erreur.")
    sys.exit()
    
if heure_12 == "12:00AM":
    print("00 : 00")
elif heure_12 == "12:00PM":
    print("12 : 00")
else:
    print(heure_24,":",minutes)