import tkinter as tk

class Spiel():
    def __init__(self):
        self.fenster = tk.Tk()

        self.fenster.config(bg='royalblue')
        self.fenster.title('Dynamische Objekte in tkinter')

        self.feld = tk.Canvas(self.fenster, width=500, height=500, bd=0, bg='pale turquoise')
        self.feld.pack()

        s = Sternchen(self.feld)
        k = Kreis(self.feld)

        self.fenster.bind('<KeyPress-Right>', lambda e: k.right())
        self.fenster.bind('<KeyPress-Left>', lambda e: k.left())
        self.fenster.bind('<KeyPress-Up>', lambda e: k.up())
        self.fenster.bind('<KeyPress-Down>', lambda e: k.down())

        self.fenster.bind('d', lambda e: s.right())
        self.fenster.bind('a', lambda e: s.left())
        self.fenster.bind('w', lambda e: s.up())
        self.fenster.bind('s', lambda e: s.down())

        self.fenster.mainloop()

class Spieler():
    def __init__(self,feld):
        self.feld = feld

    def geh(self):
        self.feld.move(self.figur, self.x, self.y)
        self.feld.after(100, self.geh) # Wiederholen, nach 100 Millisekunden

    def right(self):
        self.x = 5
        self.y = 0
        self.geh()

    def left(self):
        self.x = -5
        self.y = 0
        self.geh()

    def up(self):
        self.x = 0
        self.y = -5
        self.geh()

    def down(self):
        self.x = 0
        self.y = 5
        self.geh()

class Sternchen(Spieler):
    def __init__(self, feld):
        super().__init__(feld)
        self.points = [0, 50, 40, 40, 50, 0, 60, 40, 100, 50, 60, 60, 50, 100, 40, 60]
        self.figur = self.feld.create_polygon(self.points, fill='red', width=2, outline='purple')
        self.feld.move(self.figur, 0, 0)

class Kreis(Spieler):
    def __init__(self, feld):
        super().__init__(feld)
        self.figur = self.feld.create_oval(0, 0, 50, 50, fill='red', width=2, outline='purple')
        self.feld.move(self.figur, 450, 450)

Spiel()

