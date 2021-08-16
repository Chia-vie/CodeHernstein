from schere_stein_papier_chrisi import ssp

# Begrüßung
print('Hallo!')

nochmal = 'ja'
while nochmal != 'nein':
    # User wählt
    userwahl = input(f'Wähle Schere, Stein oder Papier!').upper()
    ssp(userwahl)
    nochmal = input('Nochmal?').lower()