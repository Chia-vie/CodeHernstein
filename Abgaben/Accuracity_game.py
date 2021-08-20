import tkinter as tk
import random
fenster = tk.Tk()
fenster.config(bg = 'gray100')
fenster.title('Dynamische Objekte in tkinter')
feld = tk.Canvas(fenster, width=1920, height=1080, bd=0, bg='pale turquoise')
feld.pack()
random_rectanglex1 = random.randint(100, 1000)
random_rectangley1 = random.randint(500, 800)
random_rectanglex2 = random.randint(100, 1000)
random_rectangley2 = random.randint(500, 800)
counter = tk.IntVar()

def clicked(*args):
    global random_rectangley1
    global random_rectanglex1
    global random_rectangley2
    global random_rectanglex2
    counter.set(counter.get() + 1)
    feld.delete("all")
    rectangle1 = feld.create_rectangle(random_rectanglex1, random_rectangley1, random_rectanglex2, random_rectangley2, fill="red",tags="rectangle1")
    random_rectanglex1 = random.randint(100, 1000)
    random_rectangley1 = random.randint(500, 800)
    random_rectanglex2 = random.randint(100, 1000)
    random_rectangley2 = random.randint(500, 800)

rectangle1 = feld.create_rectangle(random_rectanglex1, random_rectangley1, random_rectanglex2, random_rectangley2, fill="red",tags="rectangle1")
Zaehler=tk.Label(fenster, font=('Gothic', 24, 'bold'), textvariable=counter, width=10, height=5, fg="gray100", bg="gray1")
Zaehler.place(x=0, y=0)
feld.tag_bind("rectangle1","<Button-1>",clicked)


fenster.mainloop()
