x = "a"
frage_count = 0
punktestand = 0
versuche = 0
# Begrüßung
print('Willkommen!')

# Frage stellen
print(f'Hier kommt deine {frage_count+1}. Frage: ')

while x == "a":
    if punktestand == 2:
        print("Super! Du hast alle Fragen erraten!")
        quit()
    frage1 = 'Wie heißt die Hauptstadt von den USA?'
    frage2 = 'Wo leben Eisbären'
    antwort1 = 'WASHINGTON'
    antwort2 = 'ARKTIS'
    tipp11 = 'Es ist nicht New York.'
    tipp12 = 'Sie wurde nach dem ersten Präsidenten benannt.'
    tipp21 = 'Es ist dort sehr kalt'
    tipp22 = 'Die Region befindet sich um den Nordpol'
    fragen = [frage1,frage2]
    antworten = [antwort1,antwort2]
    #tipps = {'1': [tipp11, tipp12]}
    #tipps2 = {'1': [tipp21], '2': [tipp22]}
    antwort = input(fragen[frage_count]+'\n')
    if antwort.upper() == antworten[frage_count]:
        punktestand += 1 # eins dazuzählen
        frage_count += 1 # eins dazuzählenj
        versuche = 0
        print('Super! Du hast es erraten!')
        print(f'Dein neuer Punktestand ist: {punktestand}')
    else:
        versuche += 1
        print('Leider nicht richtig.')
        if versuche == 2 and punktestand == 0:
            # Tipp geben
            print(f'Hier ist ein Tipp für dich: \n {tipp12}')
        elif versuche == 4 and punktestand == 0:
            print(f'Hier ist ein Tipp für dich: \n {tipp11}')
        elif versuche == 10:
            print("Bischt du deppert?!?!?!")
            x = "b"
        if versuche == 2 and punktestand == 1:
            # Tipp geben
            print(f'Hier ist ein Tipp für dich: \n {tipp21}')
        elif versuche == 4 and punktestand == 1:
            print(f'Hier ist ein Tipp für dich: \n {tipp22}')
        elif versuche == 10 and punktestand == 1:
            print("Bischt du deppert?!?!?!")
            x = "b"
