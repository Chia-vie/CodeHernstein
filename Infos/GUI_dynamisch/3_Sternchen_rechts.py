import tkinter as tk

class Sternchen():
    def __init__(self, fenster):
        self.feld = tk.Canvas(fenster, width=500, height=500, bd=0, bg='pale turquoise')
        self.feld.pack()
        self.points = [0, 50, 40, 40, 50, 0, 60, 40, 100, 50, 60, 60, 50, 100, 40, 60]
        self.form = self.feld.create_polygon(self.points, fill='red', width=2, outline='purple')
        self.x = 0
        self.y = 0
        self.feld.move(self.form, self.x, self.y)

    def right(self):
        self.x = 5
        self.y = 0
        self.feld.move(self.form, self.x, self.y)
        self.feld.after(100, self.right)  # Wiederholen, nach 100 Millisekunden

fenster = tk.Tk()
fenster.config(bg = 'royalblue')
fenster.title('Dynamische Objekte in tkinter')

sterndi = Sternchen(fenster)

# Pfeiltasten
#fenster.bind('<KeyPress-Left>', lambda e: bewegen())
fenster.bind('<KeyPress-Right>', lambda e: sterndi.right())
#fenster.bind('<KeyPress-Up>', lambda e: bewegen())
#fenster.bind('<KeyPress-Down>', lambda e: bewegen())

fenster.mainloop()