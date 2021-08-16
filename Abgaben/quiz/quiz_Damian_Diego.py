
frage1 = 'Wie heißt die Hauptstadt von den USA?'
frage2 = 'Wo leben Eisbären?'
frage3 = 'Wie viele Schüler sind wir?'
frage4 = 'Was war die erste Frage?'

antwort1 = 'WASHINGTON'
antwort2 = 'ARKTIS'
antwort3 = '12'
antwort4 = 'WIE HEIßT DIE HAUPTSTADT VON DEN USA'

tipp11 = 'Es ist nicht New York.'
tipp12 = 'Sie wurde nach dem ersten Präsidenten benannt.'
tipp21 = 'Es ist dort sehr kalt'
tipp22 = 'Die Region befindet sich um den Nordpol'
tipp31 = 'mehr als 10'
tipp32 = 'weniger als 15'
tipp41 = 'es ging um eine Hauptstadt'
tipp42 = 'Das Land war die USA'

fragen = [frage1,frage2,frage3,frage4]
antworten = [antwort1,antwort2,antwort3,antwort4]
tipps = {'1': [tipp11,tipp12], '2': [tipp21,tipp22], '3': [tipp31,tipp32], '4': [tipp41,tipp42]}

frage_count = 0
punktestand = 0
versuche = 0

print('Willkommen!')

while frage_count<len(fragen):
    print(f'Hier kommt deine {frage_count+1}. Frage: ')

    antwort = input(fragen[frage_count]+'\n')

    if antwort.upper() == antworten[frage_count]:
        punktestand += 1
        frage_count += 1
        versuche = 0
        print('Super! Du hast es erraten!')
        print(f'Dein neuer Punktestand ist: {punktestand}')
    else:
        versuche += 1
        print('Leider nicht richtig.')
        if versuche > 1:
            punktestand -= 1
            print(f'Du hast einen punkt verloren, aber hier ist ein Tipp für dich: \n {tipps[str(frage_count+1)][versuche-2]}')


print(f'Du hast das Quiz bestanden mit einem Punktestand von {punktestand} Punkten')
