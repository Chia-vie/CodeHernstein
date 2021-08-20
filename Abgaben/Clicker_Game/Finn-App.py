import tkinter as tk
import time
# from tkinter import *
from PIL import ImageTk, Image


time.sleep(0.00001)
app = tk.Tk()
app.geometry("1920x1080")
app.title("Clicker Game")

# def knopfgedrückt(text):
# global out
# die verschiedenen outputs einer Variable zuordnen
# out.set
# app.update_idletasks()


# beschreibung = tk.Label(app, text='Willkommen! Hier kannst du einen Knopf drücken!', font=('Helvetica', 16, 'bold'),
# bg='pale turquoise', fg='black', width = 40, height=2)

header = tk.Label(app, text='Füttere Foxi', font=('Gothic', 24, 'bold'), bg='gray1', fg='green2', width=40, height=2)
header.pack()
app.config(bg='gray1')


# out = tk.StringVar()
# out.set('Drück den Knopf!')

# rahmen = tk.Frame(app, bg='purple')
# rahmen.pack(side='top', padx='10', pady='30')
# knopf = tk.Button(app, text='0', font=('Gothic',20, 'bold'),
# fg='blue4', width=20, height=5, command=lambda: knopfgedrückt('Chrisi'))
# knopf.pack()

counter = tk.IntVar()
Generator1 = False

def onclick():
    counter.set(counter.get() + 1)
def whenclick():
    global Generator1
    Generator1 = True

# def do(event):
# print("Button Clicked!")
# counter.set(counter.get() + 1)
# ...
if Generator1 == True:
    while True:
        time.sleep(10)
        counter.set(counter.get() + 1)

img = ImageTk.PhotoImage(Image.open("Unbenannt.png"))
# tk.Button = Label(app, image = img, activeforeground="green2", fg="green2", activebackground="gray1", bg="gray1", width=100, height=50).pack()

# tk.Button.bind('<Button-1>', do)

button1 = tk.Label(app, font=('Gothic', 24, 'bold'), text="Hundefutter:", bg="gray1", fg="gray100", width=100)
Zaehler=tk.Label(app, font=('Gothic', 24, 'bold'), textvariable=counter, width=10, height=5, fg="gray100", bg="gray1").pack()
Clicks_dazu=tk.Button(app, image=img, command=onclick, activeforeground="green2", fg="green2", activebackground="gray1", bg="gray1", width=590, height=700).pack()
Hund1 = tk.Button(app, command=Generator1, activeforeground="green2", fg="green2", activebackground="gray1", bg="gray1", width=100, height=100)
button1.place(x=-80, y=140)
Hund1.place(x =-120, y=140)
# tk.Button



app.mainloop()
