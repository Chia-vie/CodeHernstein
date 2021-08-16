'''
Schreibe eine Funktion um (physikalische) Größen umzuwandeln:
Z.B.
°Celsius / Kelvin / °Fahrenheit
Liter / Kubikmeter / Kubikzentimeter
Lichtjahre / Kilometer / Parsec
'''

# Ein Beispiel: Hier wird ein Wert der Einheit FLUP, BLUP oder SNUP in die jeweils anderen Einheiten umgerechnet
def konverter(wert, user_einheit):
    user_einheit = user_einheit.upper() # In upper case String umwandeln, für Vergleichbarkeit
    einheiten = ['CM','M','KM']
    if user_einheit == 'CM':
        var1 = wert * 100 # Umrechnen in BLUP
        var2 = wert * 10_000 # Umrechnen in SNUP

    elif user_einheit == 'M':
        var1 = wert / 100 # Umrechnen in FLUP
        var2 = wert * 1000 # Umrechnen in SNUP

    elif user_einheit == 'KM':
        var1 = wert / 10_000# Umrechnen in FLUP
        var2 = wert / 1000# Umrechnen in BLUP

    else: # falls Einheit falsch => wird beendet ohne unteren Teil auszuführen
        return 'Tut mir leid, ich kenne diese Einheit nicht.'

    einheiten.remove(user_einheit) # Nur die nicht eingegebenen Einheiten ins Ergebnis übernehmen.
    ergebnis = dict((e,v) for e,v in zip(einheiten, (var1,var2))) # Einheiten und zugehörige Ergebnisse in Dictionary speichern
    return ergebnis

eingabe = input('Bitte hier ihre einheit eingeben: ')
eingabe2 = int(input('Bitte hier ihre Menge eingeben: '))



print(konverter(eingabe2, eingabe))





