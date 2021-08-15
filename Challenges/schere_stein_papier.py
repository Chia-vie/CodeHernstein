import random


# Zufallszahl
zzahl = random.randint(0, 2)

# Möglichkeiten
moeglichkeiten = ['SCHERE', 'STEIN', 'PAPIER']

# Auswahl aus der Liste
computerwahl = moeglichkeiten[zzahl]

# Begrüßung
print('Hallo!')

# User wählt aus
userwahl = input(f'Wähle Schere, Stein oder Papier!').upper()

# Auswahl ausgeben
print(f'Du hast {userwahl} gewählt, ich habe {computerwahl} gewählt')

# Unentschieden:
if computerwahl == userwahl:
    print('Unentschieden')
# Computer gewinnt: (Vervollständige!)

# Computer verliert: (Vervollständige!)


