import tkinter as tk
import random

class Spiel():
    def __init__(self):
        self.fenster = tk.Tk()

        self.fenster.config(bg='royalblue')
        self.fenster.title('Dynamische Objekte in tkinter')

        self.feld = tk.Canvas(self.fenster, width=500, height=500, bd=0, bg='pale turquoise')
        self.feld.pack()

        self.make_ball()

        self.fenster.bind('<KeyPress-Right>', lambda e: self.right())
        self.fenster.bind('<KeyPress-Left>', lambda e: self.left())
        self.fenster.bind('<KeyPress-Up>', lambda e: self.up())
        self.fenster.bind('<KeyPress-Down>', lambda e: self.down())

        self.fenster.mainloop()

    def make_ball(self):    #self.feld = feld
        self.points = [0, 0, 40, 40]
        self.ball = self.feld.create_oval(self.points, fill='red', width=2, outline='purple')
        self.x = random.randint(0,300)
        self.y = random.randint(0,300)
        self.feld.move(self.ball, self.x, self.y)
        self.richtung()

    def richtung(self):
        self.x = random.uniform(-1, 1)*7
        self.y = random.uniform(-1, 1)*7
        self.bewegen()

    def bewegen(self):
        self.feld.move(self.ball, self.x, self.y)
        self.grenzen()
        self.feld.after(100, self.bewegen) # Wiederholen, nach 100 Millisekunden

    def grenzen(self):
        ball_koord=self.feld.coords(self.ball)
        print(ball_koord)
        if any(x >= 500 for x in ball_koord[::2]) or any(x <= 0 for x in ball_koord[::2]):
            # rechter/linker Rand
            self.x = -self.x
            self.bewegen()
        elif any(y >= 500 for y in ball_koord[1::2]) or any(y <= 0 for y in ball_koord[1::2]):
            self.y = -self.y
            self.bewegen()
            # unterer/oberer Rand




Spiel()
