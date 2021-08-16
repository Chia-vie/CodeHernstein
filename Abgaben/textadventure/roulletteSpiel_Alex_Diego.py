import time
import random

reingehen = input('Du stehst vor einem Casiono. Gehst du rein? Ja oder nein.').upper()

if reingehen == "JA":
    time.sleep(1)
    roulette = input('Du wirst eingeladen dich zum Roulette zu setzten. Tust du es oder nicht?').upper()
    if roulette == "JA":
        time.sleep(1)
        print("Du setzt dich an den Tisch und dir ein Whisky angeboten")
        time.sleep(1)
        whisky = input("Trinkst du?").upper()
        if whisky == "JA":
            time.sleep(1)
            print("Du bist besoffen und musst ins Krankenhaus")
            quit()
        else:
            time.sleep(1)
            print("Du entscheidest dein ganzes Vermögen auf eine Farbe zu setzen und musst nun entscheiden.")
            time.sleep(1)
            print("---")
            time.sleep(1)
            farbe = input("Auf welche Farbe setzt du? (Rot oder Schwarz)").upper()
            zzahl = random.randint(0,1)
            if zzahl == 0:
                richtigeFarbe = "ROT"
            else:
                richtigeFarbe = "SCHWARZ"
            if farbe == richtigeFarbe:
                time.sleep(1)
                print("Es dreht sich")
                time.sleep(1)
                print("Du hast gewonnen und bist nun Millionär!")
                quit()
            else:
                time.sleep(1)
                print("Es dreht sich")
                time.sleep(1)
                print("Du hast verloren und stirbst als Armer!")
                quit()

    else:
        print("Du verlierst dein Geld und stirbst an Hunger")
        quit()

else:
    print('Du geizhals wirst wegen schlechtem Karma erschossen!')
    quit()
