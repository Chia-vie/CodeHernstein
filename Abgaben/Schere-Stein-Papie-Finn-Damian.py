import random
print('Sei Begrüßt. Dies ist ein Schere, Stein, Papier-bot')
x=True
while x==True:
    zzahl = random.randint(0, 2)
    moeglichkeiten = ['SCHERE', 'STEIN', 'PAPIER']
    computerwahl = moeglichkeiten[zzahl]
    userwahl = input(f'Wähle Schere, Stein oder Papier!').upper()
    print(f'Du hast {userwahl} gewählt, ich habe {computerwahl} gewählt')
    if computerwahl == "SCHERE" and userwahl == 'SCHERE':
        print('Nochmal')
        continue
    elif computerwahl == 'SCHERE' and userwahl == 'STEIN':
        print('Du hast gewonnen')
        break
    elif computerwahl == 'SCHERE' and userwahl == 'PAPIER':
        print('Ich habe gewonnen du loser')
        continue
    if computerwahl == "STEIN" and userwahl == 'STEIN':
        print('Nochmal')
        continue
    elif computerwahl == 'STEIN' and userwahl == 'PAPIER':
        print('Du hast gewonnen')
        break
    elif computerwahl == 'STEIN' and userwahl == 'SCHERE':
        print('Ich habe gewonnen, du loser')
        continue
    if computerwahl == "PAPIER" and userwahl == 'PAPIER':
        print('Nochmal')
        continue
    elif computerwahl == 'PAPIER' and userwahl == 'SCHERE':
        print('Du hast gewonnen')
        break
    elif computerwahl == 'PAPIER' and userwahl == 'STEIN':
        print('Ich habe gewonnen du loser')
        continue
