import numpy as np


class Rechner:

    def __init__(self, zahl1=False, zahl2=False):
        self.zahl1 = float(zahl1)
        if zahl2 == "pi":
            self.zahl2 = np.pi
        else:
            self.zahl2 = float(zahl2)
    # Grundrechnungsarten
    def addieren(self):
        return self.zahl1 + self.zahl2

    def subtrahieren(self):
        return self.zahl1 - self.zahl2

    def multiplitzieren(self):
        return self.zahl1 * self.zahl2

    def dividieren(self):
        return self.zahl1 / self.zahl2

    # Wurzeln und Potenzieren

    def quadrieren(self):
        return self.zahl1 ** 2

    def potenzieren(self):
        return self.zahl1 ** self.zahl2

    def quadratwurzel(self):
        return self.zahl1 ** 0.5

    def wurzel(self):
        return self.zahl1 ** (1/self.zahl2)

    # Spezialfunktionen








#x = Rechner(1,"pi")
#print(x.multiplitzieren())
