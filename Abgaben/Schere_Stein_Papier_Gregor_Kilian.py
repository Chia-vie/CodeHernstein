import random


# Zufallszahl
zzahl = random.randint(0, 2)

# Möglichkeiten
moeglichkeiten = ['SCHERE', 'STEIN', 'PAPIER']

# Auswahl aus der Liste
computerwahl = moeglichkeiten[zzahl]

# Begrüßung
print('Hallo, du Kek!')

# User wählt aus
userwahl = input(f'Wähle Schere, Stein oder Papier!').upper()

# Auswahl ausgeben
print(f'Du hast {userwahl} gewählt, ich habe {computerwahl} gewählt')

# Unentschieden:
if computerwahl == userwahl:
    print('Unentschieden')
# Computer gewinnt: (Vervollständige!)

if computerwahl == moeglichkeiten[0] and userwahl == moeglichkeiten[2]:
    print('Computer gewinnt!')
elif computerwahl == moeglichkeiten[1] and userwahl == moeglichkeiten[0]:
    print('Computer gewinnt!')
elif computerwahl == moeglichkeiten[2] and userwahl == moeglichkeiten[1]:
    print('Computer gewinnt!')

# Computer verliert: (Vervollständige!)
else:
    if userwahl == moeglichkeiten[0] and computerwahl == moeglichkeiten[2]:
        print('Spieler gewinnt!')
    elif userwahl == moeglichkeiten[1] and computerwahl == moeglichkeiten[0]:
        print('Spieler gewinnt!')
    elif userwahl == moeglichkeiten[2] and computerwahl == moeglichkeiten[1]:
        print('Spieler gewinnt!')

