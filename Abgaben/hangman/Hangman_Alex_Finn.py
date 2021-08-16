import random
import string
import numpy as np
x = ("a")
y = 1
# Mögliche Wörter
woerter = 'Quizshow, Vollmond, Hollywood, Puderzucker, Dumpfbacke, ' \
         'Kuddelmuddel, Hund, Oper, Mond, Mars, Quiz, Auto, Zebra, ' \
         'Venus, Zwiebelsuppe, Nahrungsmittel, Finanzamt'

# String in Liste umwandeln
woerter = list(woerter.split(', '))

# Zufälliges Wort auswählen
wort = list(woerter[random.randint(0,len(woerter))].upper())

# In numpy array umwandeln
wort = np.array(wort)

# zu Testzwecken
print(wort)

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
print('Errätst du mein Wort?')
print(*wort_display)
while x == "a":
    # Buchstaben abfragen
    guess = input('Gib einen Buchstaben ein \n').upper()
    if guess not in richtig:
        y += 1
    # Falls der Buchstabe noch nicht geraten wurde
    if not guess in geraten:
        geraten.add(guess) # hinzufügen
        alphabet.discard(guess) # entfernen
        if y == 2:
            print('''
            
            
            
            
            ________
            ''')
        if y == 3:
            print('''
            |
            |
            |
            |
            |________
            ''')
        if y == 4:
            print('''
             __ __
            |
            |
            |
            |
            |________
            ''')
        if y == 5:
            print('''
             __ __
            |     |
            |     0
            |
            |
            |________
            ''')
        if y == 6:
            print('''
             __ __
            |     |
            |     0
            |     Y
            |    / \\
            |________
            ''')
            quit()


        # Falls der Buchstabe im Wort ist
        if guess in richtig:
            print('Super!')
            ind = np.where(wort == guess) # Nachsehen an welcher Stelle der Buchstabe steht
            wort_display[ind]=''+guess+'' # In der Anzeige austauschen
            print(*wort_display) # Anzeigen
            richtig.discard(guess) # aus den richtigen entfernen
    else:
        print(f'Du hast bereits den Buchstaben {guess} versucht.')


