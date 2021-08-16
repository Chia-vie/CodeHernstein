def Celsius_Kelvin_Wandler():
    if einheit == 'C-K':
        zahl = int(input('Wie viel soll es sein:'))
        print(zahl+273)

def Kelvin_Celsius_Wandler():
    if einheit == 'K-C':
        zahl = int(input('Wie viel soll es sein:'))
        print(zahl - 273)

def Celsius_Fahreinheit_Wandler():
    if einheit == 'C-F':
        zahl = int(input('Wie viel soll es sein:'))
        print((zahl*(9/5))+32)

def Fahreinheit_Celsius_Wandler():
    if einheit == 'F-C':
        zahl = int(input('Wie viel soll es sein'))
        print((zahl - 32 *(9/5)))



einheit = input('was suchst du:')
Celsius_Fahreinheit_Wandler()
Celsius_Kelvin_Wandler()
Fahreinheit_Celsius_Wandler()
Kelvin_Celsius_Wandler()







