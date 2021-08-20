import tkinter as tk

class Spiel():
    def __init__(self):
        self.fenster = tk.Tk()

        self.fenster.config(bg='royalblue')
        self.fenster.title('Dynamische Objekte in tkinter')

        self.feld = tk.Canvas(self.fenster, width=500, height=500, bd=0, bg='pale turquoise')
        self.feld.pack()

        self.make_sternchen()
        self.make_kreis()

        self.fenster.bind('<KeyPress-Right>', lambda e: self.right(self.sternchen))
        self.fenster.bind('<KeyPress-Left>', lambda e: self.left(self.sternchen))
        self.fenster.bind('<KeyPress-Up>', lambda e: self.up(self.sternchen))
        self.fenster.bind('<KeyPress-Down>', lambda e: self.down(self.sternchen))

        self.fenster.bind('d', lambda e: self.right(self.kreis))
        self.fenster.bind('a', lambda e: self.left(self.kreis))
        self.fenster.bind('w', lambda e: self.up(self.kreis))
        self.fenster.bind('s', lambda e: self.down(self.kreis))

        self.fenster.mainloop()

    def make_sternchen(self):    #self.feld = feld
        self.points = [0, 50, 40, 40, 50, 0, 60, 40, 100, 50, 60, 60, 50, 100, 40, 60]
        self.sternchen = self.feld.create_polygon(self.points, fill='red', width=2, outline='purple')
        self.feld.move(self.sternchen, 0, 0)

    def make_kreis(self):    #self.feld = feld
        self.kreis = self.feld.create_oval(0, 0, 50, 50, fill='red', width=2, outline='purple')
        self.feld.move(self.kreis, 450, 450)

    def geh(self, spieler):
        self.feld.move(spieler, self.x, self.y)
        #self.feld.after(100, self.geh) # Wiederholen, nach 100 Millisekunden

    def right(self, spieler):
        self.x = 5
        self.y = 0
        self.geh(spieler)


    def left(self, spieler):
        self.x = -5
        self.y = 0
        self.geh(spieler)

    def up(self, spieler):
        self.x = 0
        self.y = -5
        self.geh(spieler)

    def down(self, spieler):
        self.x = 0
        self.y = 5
        self.geh(spieler)

Spiel()

