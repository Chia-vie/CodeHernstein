def konverter(wert, user_einheit):
    user_einheit = user_einheit.upper() # In upper case String umwandeln, für Vergleichbarkeit
    einheiten = ['LJ','KM','MM']
    if user_einheit == 'LJ':
        var1 = wert * 9.461e+15 # Umrechnen in Kilometer
        var2 = wert * 9.223e+18 # Umrechnen in Millimeter

    elif user_einheit == 'KM':
        var1 = wert / 9.461e+15 # Umrechnen in Lichtjahr
        var2 = wert * 1e+6  # Umrechnen in Millimeter

    elif user_einheit == 'MM':
        var1 = wert / 9.223e+18 # Umrechnen in Lichtjahr
        var2 = wert / 1e+6 # Umrechnen in Kilometer

    else: # falls Einheit falsch => wird beendet ohne unteren Teil auszuführen
        return 'Tut mir leid, ich kenne diese Einheit nicht.'

    einheiten.remove(user_einheit) # Nur die nicht eingegebenen Einheiten ins Ergebnis übernehmen.
    ergebnis = dict((e,v) for e,v in zip(einheiten, (var1,var2))) # Einheiten und zugehörige Ergebnisse in Dictionary speichern
    return ergebnis

Einheit = input("Welche einheit willst du umrechnen Kilometer(KM), Lichtjahre(LJ) oder Millimeter(MM)\n").upper()
Menge = int(input('Wieviele?: '))
print(konverter(Menge, Einheit))
