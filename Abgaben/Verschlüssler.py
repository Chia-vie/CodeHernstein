class Verschluessler():
    def __init__(self,text):
        self.text = text
        self.codierung = (("A", ">"),("B", "<"),("C", ","),("D", "°"),("E", "."),("F", ":"),("G", ";"),("H", "@"),
                          ("I", "-"),("J", "_"),("K", "!"),("L", "§"),("M", "$"),("N", "%"),("O", "&"),("P", "4"),
                          ("Q", "/"),("R", "("),("S",")"),("T", "="),("U", "?"),("V", "´"),("W", "*"),("X", "+"),
                          ("Y", "~"),("Z", "#"))
        self.output = []
    #verschluesseln
    def verchluesseln(self):
        for letter in self.text:
            for pair in self.codierung:
                if pair[0] == letter.upper():
                    neu = pair[1]
                    self.output.append(neu)
        return self.output

    def entschluesseln(self):
        #entschluesseln
        for letter in self.text:
            for pair in self.codierung:
                if pair[1] == letter:
                    neu = pair[0]
                    self.output.append(neu)


        return self.output

"""probeobjekt = Verschluessler('')
print(probeobjekt.verchluesseln())"""

"""probeobjekt = Verschluessler('')
print(probeobjekt.entschluesseln())"""
