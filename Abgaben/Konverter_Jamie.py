'''
Schreibe eine Funktion um (physikalische) Größen umzuwandeln:
Z.B.
°Celsius / Kelvin / °Fahrenheit
Liter / Kubikmeter / Kubikzentimeter
Lichtjahre / Kilometer / Parsec
'''


def konverter(wert, user_einheit):
    user_einheit = user_einheit.lower()
    einheiten = ['celsius', 'kelvin', 'fahrenheit']
    if user_einheit == 'celsius':
        var1 = wert + 273.15
        var2 = wert  * 1.8 + 32

    elif user_einheit == 'kelvin':
        var1 = wert - 273.15
        var2 = wert (- 273.15) * 9/5 + 32

    elif user_einheit == 'fahrenheit':
        var1 = wert (- 32) * 5/9
        var2 = wert (- 32) * 5/9 + 273.15

    else:
        return 'Tut mir leid, ich kenne diese Einheit nicht.'

    einheiten.remove(user_einheit)
    ergebnis = dict((e,v) for e,v in zip(einheiten, (var1,var2)))
    return ergebnis

print(konverter(13,'celsius'))
