class Coder:
    def __init__(self, text):
        self.text = text.upper()
        self.schluessel = {'A': 35, 'B': 34, 'C': 33, 'D': 32, 'E': 31,
                           'F': 30, 'G': 29, 'H': 28, 'I': 27, 'J': 26,
                           'K': 25, 'L': 24, 'M': 23, 'N': 22, 'O': 21,
                           'P': 20, 'Q': 19, 'R': 18, 'S': 17, 'T': 16,
                           'U': 15, 'V': 14, 'W': 13, 'X': 12, 'Y': 11,
                           'Z': 10,}
    def ver(self):
        output = []
        for buchstabe in self.text:
            buchstaben_zahl = self.schluessel[buchstabe]
            output.append(buchstaben_zahl)
        outstring = ''.join(str(x) for x in output)
        return outstring

    def ent(self):
        output = []
        textlist = [self.text[i:(i+2)] for i in range(0,len(self.text),2)]
        for x in textlist:
            for key in self.schluessel:
                if self.schluessel[key] == int(x):
                    output.append(key)
        outstring = ''.join(str(x) for x in output)
        return outstring





frage = input ('Willst du Entschlüsseln oder Verschlüsseln (E,V)?')
if frage.upper() == 'V':
    text = input('Was willst du Verschlüsseln?')
    meinobjekt = Coder(text)
    print(meinobjekt.ver())

elif frage.upper() == 'E':
    text = input('Was willst du Entschlüsseln?')
    meinobjekt = Coder(text)
    print(meinobjekt.ent())

