
def l_und_kubik(Wert, Einheit):

    kubikcm = ['cm3', 'cm³', 'cm^3', 'cm**3', 'kubikzentimeter']
    kubikm = ['m3', 'm³', 'm^3', 'm**3', 'kubikmeter']
    liter = ['l', 'liter']
    if Einheit.lower() in liter:
        cm3 = Wert*1000
        m3 = Wert/1000
        print(f'Dass sind {cm3} cm³ bzw. {m3} m³.')
    elif Einheit.lower() in kubikcm:
        m3 = Wert/1000000
        lit = Wert/1000
        print(f'Dass sind {m3} m³ bzw. {lit} Liter.')
    elif Einheit.lower() in kubikm:
        cm3 = Wert*1000000
        lit = Wert*1000
        print(f'Dass sind {cm3} cm³ bzw. {lit} Liter.')
    else:
        print('Du musst einen Wert und eine Einheit eingeben.')


l_und_kubik(23, 'l')

