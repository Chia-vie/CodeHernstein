'''
author: Christine Ackerl
date: 20.07.2021
Das ist ein unvollständiges Tic-Tac-Toe Spiel.
Kannst du es vervollständigen?
'''

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

# Begrüßung
print('Hallo! Spielen wir Tic Tac Toe!')
spieler1 = input("Spieler 1. Wie heißt du?")
spieler2 = input("Spieler 2. Wie heißt du?")

print(f'{spieler1}, du bist X')
print(f'{spieler2}, du bist O')

# spielfeld ausgeben
print(f'''
Hier ist euer Spielfeld:
{spielfeld}
Spieler*in 1, du beginnst. 
''')

symbol = 'X'



while True:

    # Spielerin 1 macht einen Zug
    if symbol == "X":
        zug = input(f'{spieler1}, in welches Feld möchtest du dein {symbol} setzen? \n')
    else:
        zug = input(f'{spieler2}, in welches Feld möchtest du dein {symbol} setzen? \n')
    # Im spielfeld wird die entsprechende Zahl durch ein X ersetzt
    spielfeld = spielfeld.replace(zug, symbol)
    # Der Spielzug wird in der Liste der spielzuege gespeichert
    spielzuege[int(zug)-1] = symbol
    # Neues spielfeld ausgeben
    print(spielfeld)


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
        print(f'{symbol} DU HAST GEWONNEN! GRATULIERE!')

    if symbol == 'X':
        symbol = 'O'
    else:
        symbol = 'X'

    if all(x in ["X", "0"] for x in spielzuege)
        quit()


