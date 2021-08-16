'''
author: Horsti Horst based on work by Christine Ackerl
'''

import random

def ssp(userwahl):
    # Möglichkeiten
    moeglichkeiten = ['SCHERE', 'STEIN', 'PAPIER']

    # Alle möglichen Kombinationen die zu Gewinn führen
    gewinn=[['SCHERE','PAPIER'],['STEIN','SCHERE'],['PAPIER','STEIN']]

    # Computer wählt zufällig
    zzahl = random.randint(0, 2)
    computerwahl = moeglichkeiten[zzahl]

    # Auswahl ausgeben
    print(f'Du hast {userwahl} gewählt, ich habe {computerwahl} gewählt')

    paar = [computerwahl, userwahl]

    # Unentschieden:
    if computerwahl == userwahl:
        print('Unentschieden')

    elif [computerwahl,userwahl] in gewinn:
        print('HAHA ich habe gewonnen')

    elif [userwahl,computerwahl] in gewinn:
        print('Mähhhh ich hab verloren')

