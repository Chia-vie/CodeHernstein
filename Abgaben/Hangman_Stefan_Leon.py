import random
import string
import numpy as np

(Versuche) = int(1)

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
# print(wort)

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

while Versuche > 0:

    # Buchstaben abfragen
    guess = input('Gib einen Buchstaben ein \n').upper()

    # Falls der Buchstabe noch nicht geraten wurde
    if not guess in geraten:
        geraten.add(guess) # hinzufügen
        alphabet.discard(guess) # entfernen

        # Falls der Buchstabe im Wort ist
        if guess in richtig:
            print('Super!')
            ind = np.where(wort == guess) # Nachsehen an welcher Stelle der Buchstabe steht
            wort_display[ind]=''+guess+'' # In der Anzeige austauschen
            print(*wort_display) # Anzeigen
            richtig.discard(guess) # aus den richtigen

        else:
            Versuche += 1
            if Versuche == 2:
                print('''
                
                



                _________
                ''')
                print(f'Das ist dein {Versuche}ter Versuch.')

            elif Versuche == 3:
                print('''

                |
                |
                |
                |
                |________
                ''')
                print(f'Das ist dein {Versuche}ter Versuch.')

            elif Versuche == 4:
                print('''
                 __ __
                | 
                |
                |
                |
                |________
                ''')

                print(f'Das ist dein {Versuche}ter Versuch.')

            elif Versuche == 5:
                print('''
                 __ __
                |_/   |
                |
                |
                | 
                |________
                ''')

                print(f'Das ist dein {Versuche}ter Versuch.')

            elif Versuche == 6:
                print('''
                 __ __
                |_/   |
                |     0
                |
                | 
                |________
                ''')

                print(f'Das ist dein {Versuche}ter Versuch.')

            elif Versuche == 7:
                print('''
                 __ __
                |_/   |
                |     0
                |     Y
                |
                |________
                ''')

                print(f'Das ist dein {Versuche}ter Versuch.')

            elif Versuche == 8:
                print('''
                 __ __
                |_/   |
                |    \\0/
                |     Y
                |    / \\
                |________

                GAME OVER''')

                break

    else:
        print(f'Du hast bereits den Buchstaben {guess} versucht.')














