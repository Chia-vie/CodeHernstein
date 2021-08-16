'''
author: Christine Ackerl
date: 20.07.2021
So ähnlich könnte dein Text-Adventure beginnen.
Welches Abenteuer wartet auf uns?
'''

import time

# Begrüßung

print('''
       
      /| 
*    / |    *
    /  |
   (   |  *
    \\  |
     \\ |
   *  \\|     *
       v
''')
time.sleep(1)
print('Guten Abend.')
time.sleep(1)
print('Es wird bald dunkel und wir haben einen weiten Weg vor uns.')
time.sleep(1)
weiter = input('Bist du sicher, dass du mutig genug für dieses Abenteuer bist? \n').upper()
time.sleep(1)
if weiter != 'JA':
    print('OMG YES DADDY HOOO-YA.')
    quit()
print('Gut. Ich bin beruhigt einen so mutigen Menschen an meiner Seite zu haben. Es wird sicher nicht einfach.')
name = input('Sage mir, wie darf ich dich ansprechen?\n')
time.sleep(1)
print(f'So soll es sein, {name}.')
time.sleep(1)
print('Komm, wir haben keine Zeit zu verlieren.')
time.sleep(1)
print('''
      / \\    
     /   \\
    /o    \\
www/ooo    \\www
     Y
''')
time.sleep(1)
pfad = input('Siehst du den Berg dort vorne? Was meinst du, sollen wir ihn überqueren (q) oder lieber herumgehen? (h)\n').upper()
time.sleep(1)
if pfad == 'Q':
    print('Das wird ein steiler Weg. Aber wir werden es schaffen.')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    wasser = input('Puh... Das war anstrengend. Ich brauche etwas zu trinken. Hast du Wasser dabei?\n').upper()
    time.sleep(1)
    if wasser == "JA":
        print("Nice!, dann können wir ja weitergehen")
        time.sleep(1)
        print("Unten Angekommen...")
        time.sleep(1)
        print('Es ist so dunkel, ich kann überhaupt nichts sehen.')
        time.sleep(1)
        print('Oh! Sieh nur! Da vorne ist ein Licht!')
        licht = input('Sollen wir hingehen? \n').upper()
    if wasser != 'JA':
        idee=input('Oh nein... Was sollen wir nur machen?\n')
        time.sleep(1)
        print(f'Du meinst es hilft wenn wir {idee}?')
        time.sleep(1)
        print(f'Oh! Sieh nur! da vorne ist ein Brunnen!')
        time.sleep(1)
        print('''
           ___
          |  *
          |  *
         _|________
        |          |
        |          |
        |          |
        ''')
        trinken=input('Meinst du das Wasser ist in Ordnung?\n').upper()
        time.sleep(1)
        if trinken == 'JA':
            print('WÜRG')
            time.sleep(1)
            print('WORGXKWTIGJASDLFJ!!!')
            time.sleep(1)
            print('GAME OVER')
            quit()
        elif trinken == "NEIN":
            print("Okay dann werden wir wohl für Grundwasser buddeln müssen")
            time.sleep(5)
            print("Oh nein du bist in das Loch gefallen")
            print("GAME OVER")
            quit()
        else:
            print("Bist du etwa ein Alien?!?!??!")
            print("SECRET ENDING. NICE JOB")
            quit()
elif pfad == 'H':
    print('Das wird uns viel Zeit kosten, aber vielleicht ist es besser so.')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('Wir sind fast angekommen.')
    time.sleep(1)
    print('...')
    time.sleep(1)
    print('Drei Stunden später')
    time.sleep(1)
    print('Es ist so dunkel, ich kann überhaupt nichts sehen.')
    time.sleep(1)
    print('Oh! Sieh nur! Da vorne ist ein Licht!')
    licht = input('Sollen wir hingehen? \n').upper()
    if licht == 'JA':
        print("OH NEIN DA IST JACK DER RIPPER")
        time.sleep(1)
        print('STAB!')
        print('GAME OVER!')
        quit()
    else:
        time.sleep(1)
        print('Du hast wahrscheinlich recht. Lass uns lieber in der Dunkelheit bleiben.')
        time.sleep(1)
        streichholz = input("Du hast nicht zufällig ein Streihholz dabei, oder?\n".upper())
        if streichholz == "Ja" or "Doch":
            print("Ohne weitere Vorkommnisse kommt ihr sicher zurück in euer Dorf und werdet gefeiert weil ihr Silvester seid")
            time.sleep(1)
            print("GOOD ENDING")
            quit()
        else:
            print("Oh nein wie werden wir je wieder zurückfinden")
            time.sleep(1)
            print("Ihr verirrt euch auf ewig und werded nie wieder gefunden")
            print("GAME OVER")
            quit()
