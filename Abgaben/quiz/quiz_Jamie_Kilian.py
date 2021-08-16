import random
frage1 = 'Wie heißt die Hauptstadt von den USA?'
frage2 = 'Wo leben Eisbären'
frage3 = "Wie viele Kontinente gibt es(Zahl)?"
antwort1 = 'WASHINGTON'
antwort2 = 'ARKTIS'
antwort3 = "7"
tipp11 = 'Es ist nicht New York.'
tipp12 = 'Sie wurde nach dem ersten Präsidenten benannt.'
tipp21 = 'Es ist dort sehr kalt.'
tipp22 = 'Die Region befindet sich um den Nordpol.'
tipp31 = "Die Zahl ist größer als Fünf."
tipp32 = "Drei davon sind Europa, Australien und Afrika."
fragen = [frage1,frage2,frage3]
antworten = [antwort1,antwort2,antwort3]
tipps= {'1': [tipp11,tipp12], '2': [tipp21,tipp22], '3':[tipp31,tipp32]}
frage_count = 0
punktestand = 0
versuche = 0
print('Willkommen!')
while versuche <=9:
    print(f'Hier kommt deine {frage_count+1}. Frage: ')
    antwort = input(fragen[frage_count]+"\n")
    if antwort.upper() == antworten[frage_count]:
        punktestand += 1
        frage_count += 1
        versuche = 0
        print('Super! Du hast es erraten!')
        print(f'Dein neuer Punktestand ist: {punktestand}')
        if punktestand == 3:
            print("Toll, du hast das Quiz gewonnen!!!")
            quit()
    else:
        versuche += 1
        print('Leider nicht richtig.')
    if versuche == 2:
        zzahl = random.randint(0,1)
        print(f'Hier ist ein Tipp für dich: \n {tipps[str(frage_count+1)][zzahl]}')
