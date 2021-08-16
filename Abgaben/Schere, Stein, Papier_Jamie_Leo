import random
zzahl = random.randint(0, 2)
moeglichkeiten = ['SCHERE', 'STEIN', 'PAPIER']
computerwahl = moeglichkeiten[zzahl]
print('Hallo!')
userwahl = input(f'Wähle Schere, Stein oder Papier!').upper()
print(f'Du hast {userwahl} gewählt, ich habe {computerwahl} gewählt')
if computerwahl == userwahl:
    print('Unentschieden')
elif computerwahl == 'SCHERE' and userwahl == 'PAPIER' or computerwahl == 'PAPIER' and userwahl == 'STEIN' or computerwahl == 'STEIN' and userwahl == 'SCHERE':
    print(f"Haha, Ich habe gewonnen!")
else:
    print("Schade, Du hast gewonnen!")
