import random

print("Hallo! Du bist am Ende angekommen. du hast keine Chance gegen mich")


moeglichkeiten = ["SCHERE", "STEIN", "PAPIER"]


while True:
    computerzahl = random.randint(0,2)
    computerwahl = moeglichkeiten[computerzahl]
    userwahl = input("Wähle jetzt Schere, Stein oder Papier!:").upper()
    if userwahl == computerwahl:
        print(f'Unendschieden. Der Computer hat {computerwahl} und du hast {userwahl}.')
    elif userwahl == 'SCHERE' and computerwahl == 'PAPIER' or userwahl == 'PAPIER' and computerwahl == 'STEIN'  or userwahl == 'STEIN' and computerwahl == 'SCHERE':
        print(f'Du hast Gewonnen. Der Computer hat {computerwahl} und du hast {userwahl}.')
    else:
        print(f'Du hast Verloren. Der Computer hat {computerwahl} und du hast {userwahl}.')



