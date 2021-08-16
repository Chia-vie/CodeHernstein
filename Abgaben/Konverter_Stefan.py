
'''
Schreibe eine Funktion um (physikalische) Größen umzuwandeln:
Z.B.
°Celsius / Kelvin / °Fahrenheit
Liter / Kubikmeter / Kubikzentimeter
Lichtjahre / Kilometer / Parsec
'''

print('Hier siehst du, wie viele Items du von den anderen brauchst, um gleich viel im Ofen im Ofen zu schmelzen, '
      'wie das, welches du eingibst (Lavaeimer, Kohle, und Holzbretter).')

# Ein Beispiel: Hier wird ein Wert der Einheit FLUP, BLUP oder SNUP in die jeweils anderen Einheiten umgerechnet
def konverter(wert, user_einheit):
    user_einheit = user_einheit.upper()  # In upper case String umwandeln, für Vergleichbarkeit
    einheiten = ['WODDENLOG', 'COAL', 'LAVABUCKET']
    if user_einheit == 'WODDENLOG':
        var1 = wert / 5.33333  # Umrechnen in Coal
        var2 = wert / 66.66667  # Umrechnen in LavaBucket

    elif user_einheit == 'COAL':
        var1 = wert * 5.33333  # Umrechnen in WoddenLog
        var2 = wert / 12.5  # Umrechnen in LavaBucket

    elif user_einheit == 'LAVABUCKET':
        var1 = wert * 66.66667  # Umrechnen in WoddenLog
        var2 = wert * 12.5  # Umrechnen in Coal

    else:  # falls Einheit falsch => wird beendet ohne unteren Teil auszuführen
        return 'Tut mir leid, ich kenne diese Einheit nicht.'

    einheiten.remove(user_einheit)  # Nur die nicht eingegebenen Einheiten ins Ergebnis übernehmen.
    ergebnis = dict(
        (e, v) for e, v in zip(einheiten, (var1, var2)))  # Einheiten und zugehörige Ergebnisse in Dictionary speichern
    return ergebnis

DeinWert = input('Welche Anzahl im Verhältinis willst du haben?')
DeinWert = int(DeinWert)
if DeinWert >= 0:
    DeineEinheit = input('und was wählst du (WoodenLog, Coal, Lava Bucket)?')

print(konverter(DeinWert , DeineEinheit))