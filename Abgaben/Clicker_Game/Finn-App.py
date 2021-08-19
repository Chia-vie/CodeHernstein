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

header = tk.Label(app, text='Clicker Game', font=('Gothic', 24, 'bold'), bg='gray1', fg='red2', width=40, height=2)
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


def onclick():
    counter.set(counter.get() + 1)

# def do(event):
# print("Button Clicked!")
# counter.set(counter.get() + 1)
# ...


img = ImageTk.PhotoImage(Image.open("Unbenannt.png"))
# tk.Button = Label(app, image = img, activeforeground="green2", fg="green2", activebackground="gray1", bg="gray1", width=100, height=50).pack()

# tk.Button.bind('<Button-1>', do)


tk.Label(app, textvariable=counter, width=200, height=5, fg="gray100", bg="gray1").pack()
tk.Button(app, image=img, command=onclick, activeforeground="green2", fg="green2", activebackground="gray1", bg="gray1", width=590, height=700).pack()
# tk.Button

app.mainloop()
