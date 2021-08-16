frage1 = 'Wie heißt die Hauptstadt von den USA?'
frage2 = 'Wo leben Eisbären?'

# Richtige Antworten (Großbuchstaben, für Vergleich mit User-Eingabe)
antwort1 = 'WASHINGTON'
antwort2 = 'ARKTIS'

# Tipps um die Antworten zu finden
tipp11 = 'Es ist nicht New York.'
tipp12 = 'Sie wurde nach dem ersten Präsidenten benannt.'

tipp21 = 'Es ist dort sehr kalt'
tipp22 = 'Die Region befindet sich um den Nordpol'

# Alle Fragen und Antworten in Liste speichern
fragen = [frage1,frage2]
antworten = [antwort1,antwort2]
# Alle Tipps in Dictionary speichern
tipps = {'1': [tipp11,tipp12], '2': [tipp21,tipp22]}
tippsgegeben = 0
# Anzahl der bereits gestellten Fragen
frage_count = 0
# Punktestand
punktestand = 0
# Anzahl der Versuche
versuche = 0


# Begrüßung
print('Willkommen!')

fertig = 'falsch'

while fertig == 'falsch':
    print(f'Hier kommt deine {frage_count+1}. Frage: ')
    antwort = input(fragen[frage_count]+'\n')
    if antwort.upper() == antworten[frage_count]:
        punktestand += 1 # eins dazuzählen
        frage_count += 1 # eins dazuzählen
        versuche = 0
        tippsgegeben = 0
        print('Du hast es geschafft!')
        print(f'Dein neuer Punktestand ist: {punktestand}')

    else:
        versuche += 1
        print('Leider nicht richtig.')
        if versuche == 2:
            # Tipp geben
            print(f'Hier ist ein Tipp für dich: \n {tipps[str(frage_count+1)][tippsgegeben]}')
            tippsgegeben += 1
            versuche = 0


         if punktestand == 2:
            print('Du hast beide Fragen richtig beantwortet!')
            quit()
        elif versuche == 2:
            print('Du bist sehr schlecht bitte lerne mehr!')
            fertig = 'richtig'
            versuche += 1
            if versuche == 2:
                print('Du bist sehr schlecht bitte lerne mehr!')

