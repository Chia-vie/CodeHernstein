import time
geld=100000
print("""Eine neue Saison fängt an und damit auch das alljährliche Rennen. Doch du hast noch kein Auto""")
#Autokauf
print("""
Du hast  100.000 Euro.
Dies sind deine Optionen:
        1. Ford Fiesta für 30.000
        2. Audi A3 für 40.000
        3. Ford Mustgang 50.000
Such dir eines aus und teile mir die Nummer mit
""")
auto="keines"
autowahl=int(input())
if autowahl == 1:
    geld=geld-30000
    print("Du willst wohl viel tunen? Also gut!")
    auto="Ford Fiesta"
elif autowahl == 2:
    geld=geld-40000
    print("Eine gute Wahl!")
    auto="Audi"
elif autowahl == 3:
    geld=geld-50000
    print("Viel Spaß auf der Rennstrecke!")
    auto="Ford Mustgang"
else:
    print("Selber schuld wenn du nicht schreiben kannst!")
    quit()
time.sleep(3)
#Tuning
print("""
Es gibt 4 Bereiche, die du verändern kannst!
    1. Bremsen
    2. Beschleunigung
    3. Max. Geschwindigkeit
    4. Handling
Jede Verbesserung kostet 10.000 Euro. Du kannst auch Attribute öfters verbessern.""")
print("""Teile uns einfach die Nummern der Attribute, die du verbessern willst, nacheinander mit. Achte darauf,
keine Abstände zu verwenden. Z.B.: 13324, wenn du 50.000 Euro zur Verfügung hast""")

bremsen=0
besch=0
gesch=0
handling=0
verbesserungen=input()
