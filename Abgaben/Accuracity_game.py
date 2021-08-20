import tkinter as tk
import random
fenster = tk.Tk()
fenster.config(bg = 'gray100')
fenster.title('Dynamische Objekte in tkinter')
feld = tk.Canvas(fenster, width=1920, height=1080, bd=0, bg='pale turquoise')
feld.pack()

counter = tk.IntVar()

def clicked(*args):
    counter.set(counter.get() + 1)
    feld.delete("all")

playbutton = feld.create_rectangle(1000, 500, 50, 1000, fill="red",tags="playbutton")
Zaehler=tk.Label(fenster, font=('Gothic', 24, 'bold'), textvariable=counter, width=10, height=5, fg="gray100", bg="gray1")
Zaehler.place(x=0, y=0)
feld.tag_bind("playbutton","<Button-1>",clicked)


fenster.mainloop()
