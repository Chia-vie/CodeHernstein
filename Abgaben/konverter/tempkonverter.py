def tempkonverter(eingabeeinheit, eingabewert, ausgabeeinheit):
    eingabemöglichkeiten=["FAHRENHEIT","CELSIUS","KELVIN","F","C","K"]
    eingabeeinheit=eingabeeinheit.upper()
    if eingabeeinheit not in eingabemöglichkeiten:
        return("Überprüfe deine Eingabe auf Tippfehler!")
    try:
        eingabewert=int(eingabewert)
    except:
        return("Überprüfe deine Eingabe auf Tippfehler!")
    ausgabeeinheit=ausgabeeinheit.upper()
    if ausgabeeinheit not in eingabemöglichkeiten:
        return("Überprüfe deine Eingabe auf Tippfehler!")
    if eingabeeinheit == "FAHRENHEIT" or eingabeeinheit == "F":
        if ausgabeeinheit == "CELSIUS" or ausgabeeinheit == "C":
            return((eingabewert-32)/1.8)
        if ausgabeeinheit == "KELVIN" or "K":
            return((eingabewert-32)/1.8+273.15)
    if eingabeeinheit == "CELSIUS" or eingabeeinheit == "C":
        if ausgabeeinheit == "FAHRENHEIT" or ausgabeeinheit == "F":
            return((eingabewert*(9/5))+32)
        if ausgabeeinheit == "KELVIN" or ausgabeeinheit == "K":
            return(eingabewert+273.15)
    if eingabeeinheit == "KELVIN" or eingabeeinheit == "K":
        if ausgabeeinheit == "CELSIUS" or ausgabeeinheit == "C":
            return(eingabewert-273.15)
        if ausgabeeinheit == "FAHRENHEIT" or ausgabeeinheit == "F":
            return((eingabewert*(9/5))-459.67)
"""
print("Willkommen zu dem Temperaturkonverter!")
einheit=input("Welche Einheit ist ihre Aussgangstemperatur?")
wert=(input("Danke! Welchen Wert hat diese?"))
ausgabe=input("Und jetzt: Welche Einheit hätten sie gerne?")

print(f"Ihr Ergebnis: {konverter(einheit,wert,ausgabe)}")"""


