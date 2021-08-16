import random
import string
import numpy as np
import time

# Mögliche Wörter
woerter = 'Quizshow, Vollmond, Hollywood, Puderzucker, Dumpfbacke, ' \
         'Kuddelmuddel, Hund, Oper, Mond, Mars, Quiz, Auto, Zebra, ' \
         'Venus, Zwiebelsuppe, Nahrungsmittel, Finanzamt'

# String in Liste umwandeln
woerter = list(woerter.split(', '))
fehler = 0

# Zufälliges Wort auswählen
wort = list(woerter[random.randint(0,len(woerter))].upper())

# In numpy array umwandeln
wort = np.array(wort)

# zu Testzwecken


# Set mit richtigen Buchstaben
# Sets enthalten keine Duplikate!
richtig = set(wort)

# Alphabet
alphabet = set(string.ascii_lowercase)

# Bereits geratene Buchstaben
geraten = set()

# Leerzeichen für jeden Buchstaben anzeigen
wort_display=np.array([' __ ']*len(wort))

# Begrüßung
print('Willkommen!')
time.sleep(1)
print('Errätst du mein Wort?')
time.sleep(1)
print(*wort_display)

# Buchstaben abfragen
while True:
    time.sleep(1)
    guess = input('Gib einen Buchstaben ein \n').upper()

    # Falls der Buchstabe noch nicht geraten wurde
    if not guess in geraten:
        geraten.add(guess) # hinzufügen
        alphabet.discard(guess) # entfernen
        # Falls der Buchstabe im Wort ist
        if guess in richtig:
            time.sleep(1)
            print('Super!')
            ind = np.where(wort == guess) # Nachsehen an welcher Stelle der Buchstabe steht
            wort_display[ind]=''+guess+'' # In der Anzeige austauschen
            time.sleep(1)
            print(*wort_display) # Anzeigen
            richtig.discard(guess) # aus den richtigen entfernen
            if len(richtig) == 0:
                time.sleep(2)
                print('VICTORY!')
                break
        else:
            fehler += 1
            time.sleep(1)
            print('Ups, das war wohl nix.')
            if fehler == 1:
                time.sleep(1)
                print('''
                |________''')
            if fehler == 2:
                time.sleep(1)
                print('''
                |    / \\
                |________
                    ''')
            if fehler == 3:
                time.sleep(1)
                print('''
                |    /I\\
                |    / \\
                |________
                    ''')
            if fehler == 4:
                time.sleep(1)
                print('''
                |     0
                |    /I\\
                |    / \\
                |________
                    ''')
            if fehler == 5:
                time.sleep(2)
                print('''
                 __ __
                |     |
                |     0
                |    /I\\
                |    / \\
                |________
                    ''')
                time.sleep(1)
                print('GAME OVER!')
                break
    else:
        time.sleep(1)
        print(f'Du hast bereits den Buchstaben {guess} versucht.')



