import random
import string
import numpy as np
hangman = 0
woerter = 'Quizshow, Vollmond, Hollywood, Puderzucker, Dumpfbacke, ' \
         'Kuddelmuddel, Hund, Oper, Mond, Mars, Quiz, Auto, Zebra, ' \
         'Venus, Zwiebelsuppe, Nahrungsmittel, Finanzamt'

woerter = list(woerter.split(', '))
wort = list(woerter[random.randint(0,len(woerter))].upper())
wort = np.array(wort)
print(wort)
richtig = set(wort)
alphabet = set(string.ascii_lowercase)
geraten = set()
wort_display=np.array([' __ ']*len(wort))
print('Willkommen!')
print('Errätst du mein Wort?')
print(*wort_display)
while hangman < 10:
    guess = input('Gib einen Buchstaben ein \n').upper()
    if not guess in geraten:
        geraten.add(guess)
        alphabet.discard(guess)
        hangman += 1
        if hangman == 1:
            print('''
________
''')
        if hangman == 2:
            print('''
|
|
|
|
|________
''')
        if hangman == 3:
            print('''
 __ __
|
|
|
|
|________
''')
        if hangman == 4:
            print('''
 __ __
|     |
|
|
|
|________
''')
        if hangman == 5:
            print('''
 __ __
|     |
|     0
|
|
|________
''')
            if hangman == 6:
                print('''
 __ __
|     |
|     0
|     Y
|
|________
''')
            if hangman == 7:
                print('''
 __ __
|     |
|     0
|     Y
|    /
|________
''')
            if hangman == 8:
                print('''
 __ __
|     |
|     0
|     Y
|    / \\
|________
''')
        if hangman == 9:
            print('Verkackt!!!')
            quit()
          if guess in richtig:
            print('Super!')
            ind = np.where(wort == guess)
            wort_display[ind]=''+guess+''
            print(*wort_display)
            richtig.discard(guess)
            if len(richtig) == 0:
                print("Cool, du hast mein Wort erraten!!!")
                quit()
    else:
        print(f'Du hast bereits den Buchstaben {guess} versucht.')
