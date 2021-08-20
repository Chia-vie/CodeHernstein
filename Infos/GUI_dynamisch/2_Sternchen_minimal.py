import tkinter as tk

def bewegen():
    global sternchen, x, y
    x = 10
    y = 10
    feld.move(sternchen, x, y)
    fenster.update()

# Sternchen - Punkte
points = [0, 50, 40, 40, 50, 0, 60, 40, 100, 50, 60, 60, 50, 100, 40, 60]

fenster = tk.Tk()
fenster.config(bg = 'royalblue')
fenster.title('Dynamische Objekte in tkinter')

feld = tk.Canvas(fenster, width=500, height=500, bd=0, bg='pale turquoise')
feld.pack()

sternchen = feld.create_polygon(points, fill='red', width=2, outline='purple')
x = 0
y = 0
feld.move(sternchen, x, y)

# Mögliche Tasten
#fenster.bind('<Key>', lambda e: bewegen()) # Irgendeine Taste
#fenster.bind('<Return>', lambda e: bewegen()) # Enter Taste
#fenster.bind('<Button-1>', lambda e: bewegen()) # Maustaste
#fenster.bind('<Button-2>', lambda e: bewegen())#
#fenster.bind('<Button-3>', lambda e: bewegen())#
#fenster.bind('<KeyPress-Left>', lambda e: bewegen()) # Pfeil Taste
#fenster.bind('<KeyPress-Right>', lambda e: bewegen())
#fenster.bind('<KeyPress-Up>', lambda e: bewegen())
#fenster.bind('<KeyPress-Down>', lambda e: bewegen())
#fenster.bind('a', lambda e: bewegen()) # Buchstaben Tasten
#fenster.bind('w', lambda e: bewegen())


fenster.mainloop()