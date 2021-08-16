# Ein Beispiel: Hier wird ein Wert der Einheit FLUP, BLUP oder SNUP in die jeweils anderen Einheiten umgerechnet
def konverter(wert, user_einheit):
    user_einheit = user_einheit.upper() # In upper case String umwandeln, für Vergleichbarkeit
    einheiten = ['STUNDEN','MINUTEN','SEKUNDEN']
    if user_einheit == 'STUNDEN':
        var1 = wert * 60 # Umrechnen in BLUP
        var2 = wert * 3600 # Umrechnen in SNUP

    elif user_einheit == 'MINUTEN':
        var1 = wert / 60 # Umrechnen in FLUP
        var2 = wert * 60 # Umrechnen in SNUP

    elif user_einheit == 'SEKUNDEN':
        var1 = wert / 3600 # Umrechnen in FLUP
        var2 = wert / 60 # Umrechnen in BLUP

    else: # falls Einheit falsch => wird beendet ohne unteren Teil auszuführen
        return 'Tut mir leid, ich kenne diese Einheit nicht.'

    einheiten.remove(user_einheit) # Nur die nicht eingegebenen Einheiten ins Ergebnis übernehmen.
    ergebnis = dict((e,v) for e,v in zip(einheiten, (var1,var2))) # Einheiten und zugehörige Ergebnisse in Dictionary speichern
    return ergebnis

print(konverter(13,'Sekunden'))
