'''
author: Christine Ackerl
date: 20.07.2021
Das ist ein unvollständiges Tic-Tac-Toe Spiel.
Kannst du es vervollständigen?
'''

def begruessung(spielfeld):
    # Begrüßung
    print('Hallo! Spielen wir Tic Tac Toe!')
    name1 = input('Spieler*in 1, wie heißt du?')
    print(f'Ok, {name1} du bist X')
    name2 = input('Spieler*in 2, wie heißt du?')
    print(f'Ok, {name2} du bist O')
    # spielfeld ausgeben
    print(f'''
    Hier ist euer Spielfeld:
    {spielfeld}
    {name1}, du beginnst. 
    ''')
    return name1, name2

def spielen(symbol,spielfeld,name):
    # Spielerin 1 macht einen Zug
    zug = input(f'{name}, in welches Feld möchtest du dein {symbol} setzen? \n')
    # Im spielfeld wird die entsprechende Zahl durch ein X ersetzt
    spielfeld = spielfeld.replace(zug, symbol)
    # Der Spielzug wird in der Liste der spielzuege gespeichert
    spielzuege[int(zug) - 1] = symbol
    # Neues spielfeld ausgeben
    print(spielfeld)
    return spielfeld

def gewonnen(spielzüge,name):
    # Überprüfen ob der/die Spieler*in gewonnen hat
    '''
    Das sind alle möglichen Positionen der Symbole in denen die Spielerin gewinnt:

     ___ ___ ___     ___ ___ ___     ___ ___ ___
    |_X_|_X_|_X_|   |___|___|___|   |___|___|___|
    |___|___|___|   |_X_|_X_|_X_|   |___|___|___|
    |___|___|___|   |___|___|___|   |_X_|_X_|_X_|

     ___ ___ ___     ___ ___ ___     ___ ___ ___
    |_X_|___|___|   |___|_X_|___|   |___|___|_X_|
    |_X_|___|___|   |___|_X_|___|   |___|___|_X_|
    |_X_|___|___|   |___|_X_|___|   |___|___|_X_|

     ___ ___ ___     ___ ___ ___
    |_X_|___|___|   |___|___|_X_|
    |___|_X_|___|   |___|_X_|___|
    |___|___|_X_|   |_X_|___|___|

    Dasselbe gilt natürlich auch für 'O'.
    '''
    # Wir sehen in der Liste der Spielzüge nach ob eine der Gewinnmöglichkeiten zutrifft
    if (spielzuege[0] == spielzuege[1] == spielzuege[2] or
            spielzuege[3] == spielzuege[4] == spielzuege[5] or
            spielzuege[6] == spielzuege[7] == spielzuege[8] or
            spielzuege[0] == spielzuege[3] == spielzuege[6] or
            spielzuege[1] == spielzuege[4] == spielzuege[7] or
            spielzuege[2] == spielzuege[5] == spielzuege[8] or
            spielzuege[0] == spielzuege[4] == spielzuege[8] or
            spielzuege[2] == spielzuege[4] == spielzuege[6]):
        # Falls ja, hat der/die Spielerin gewonnen
        print(f'{name} DU HAST GEWONNEN! GRATULIERE!')
        return True
    return False

# So sieht das Spielfeld am Anfang aus.
# Der/die Spieler*in kann ein Feld auswählen indem er/sie die jeweilige Zahl eingibt.
spielfeld = '''
 ___ ___ ___ 
|_1_|_2_|_3_|
|_4_|_5_|_6_|
|_7_|_8_|_9_|
'''

# Hier werden alle Spielzüge gespeichert.
# Die Zahlen werden im Lauf des Spiels durch X oder O ersetzt.
spielzuege = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = 'X'
name1, name2 = begruessung(spielfeld)
name = name1
while gewonnen(spielzuege,name) == False:
    spielfeld = spielen(symbol,spielfeld,name)
    # Wenn gerade Spieler*in 1 an der Reihe war kommt jetzt Spieler*in 2 dran, und umgekehrt
    if symbol == 'X':
        symbol = 'O'
        name = name2
    else:
        symbol = 'X'
        name = name1
    if all(zeichen in ['X','O'] for zeichen in spielzuege):
        print('Keine Züge mehr möglich')
        break

