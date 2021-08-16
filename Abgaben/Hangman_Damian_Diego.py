import random
import string
import numpy as np

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

versuche = 10

while versuche > 0:
    # Buchstaben abfragen
    guess = input('Gib einen Buchstaben ein \n').upper()
    if len(guess) > 1:
        print("Du Idiot! Du darfst nur einen Buchstaben eingeben")
        continue
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
            richtig.discard(guess) # aus den richtigen entfernen
            if len(richtig) < 1:
                print("Du hast GEWONNEN!")
                quit()
        else:
            versuche -= 1
            print(f"Nein. {guess} ist nicht in meinem Wort. Du hast noch {versuche} versuche.")
            if versuche == 9:
                print('''
                |________
                ''')
            elif versuche == 8:
                print('''
                |    
                |________
                ''')
            elif versuche == 7:
                print('''
                |     
                |    
                |________
                ''')
            elif versuche == 6:
                print('''
                |     
                |     
                |    
                |________
                ''')
            elif versuche == 5:
                print('''
                 __
                |     
                |     
                |     
                |    
                |________
                ''')
            elif versuche == 4:
                print('''
                 __ __
                |     
                |     
                |     
                |    
                |________
                ''')
            elif versuche == 3:
                print('''
                 __ __
                |     |
                |     
                |     
                |    
                |________
                ''')
            elif versuche == 2:
                print('''
                 __ __
                |     |
                |     0
                |     
                |    
                |________
                ''')
            elif versuche == 1:
                print('''
                 __ __
                |     |
                |     0
                |     Y
                |    
                |________
                ''')
    else:
        print(f'Du hast bereits den Buchstaben {guess} versucht.')



if versuche < 1:
    print("Du hast verloren!")
    print('''
                 __ __
                |     |
                |     0
                |     Y
                |    / \\
                |________
                ''')


