import tkinter as tk

class Spiel():
    def __init__(self):
        self.fenster = tk.Tk()

        self.fenster.config(bg='royalblue')
        self.fenster.title('Dynamische Objekte in tkinter')

        self.feld = tk.Canvas(self.fenster, width=500, height=500, bd=0, bg='pale turquoise')
        self.feld.pack()

        self.make_sternchen()

        self.fenster.bind('<KeyPress-Right>', lambda e: self.right())
        self.fenster.bind('<KeyPress-Left>', lambda e: self.left())
        self.fenster.bind('<KeyPress-Up>', lambda e: self.up())
        self.fenster.bind('<KeyPress-Down>', lambda e: self.down())

        self.fenster.mainloop()

    def make_sternchen(self):    #self.feld = feld
        self.points = [0, 50, 40, 40, 50, 0, 60, 40, 100, 50, 60, 60, 50, 100, 40, 60]
        self.sternchen = self.feld.create_polygon(self.points, fill='red', width=2, outline='purple')
        self.x = 0
        self.y = 0
        self.feld.move(self.sternchen, self.x, self.y)

    def geh(self):
        self.feld.move(self.sternchen, self.x, self.y)
        #self.feld.after(100, self.geh) # Wiederholen, nach 100 Millisekunden

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

Spiel()

