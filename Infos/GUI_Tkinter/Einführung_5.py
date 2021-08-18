import tkinter as tk

def knopfgedrückt(text):
    global out
    # die verschiedenen outputs einer Variable zuordnen
    out.set(f'Deine Wahl: {text}')
    fenster.update_idletasks()

def changeColor(self):
    self.b1.configure(bg="yellow")

optionen = [ "Schlumpf", "Zwerg", "Zentaur"]

# ein tkinter fenster erstellen
fenster = tk.Tk()
# Hintergrundfarbe
# Die verschiedenen Farbmöglichkeiten findet man z.B. hier:
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
fenster.config(bg='pale turquoise')

#fenster größe
#fenster.geometry('100x200')
# Name des Fensters
fenster.title('MyCoolApp')

# die Variablen für die Outputs erzeugen und auf '' = nichts setzen
out = tk.StringVar()
out.set('Drück den Knopf!')
var_opt = tk.StringVar()
var_opt.set(optionen[0])

# Dropdown Menü
opt = tk.OptionMenu(fenster, var_opt, *optionen)
opt.config(width=10, font=('Helvetica', 12))
opt.pack(side='top')

# Überschrift im Fenster
header = tk.Label(fenster,text='*******    Meine coole App    ********',
                        font=('Helvetica',24, 'bold'), bg='light blue', fg='blue4', width = 40, height=2)

#header.grid(row=0, column=0, columnspan=3, rowspan=2)
# Positionen
# row,column
#  __ __ __
# |00 01 02|
# |10 11 12|
# |20 21 22|
header.pack()

# Text im Fenster
beschreibung = tk.Label(fenster, text='Drück die Bombe!', font=('Helvetica', 16, 'bold'),
                        bg='pale turquoise', fg='black', width = 40, height=2)

#beschreibung.grid(row=2,column=0, columnspan=3, rowspan=1)
beschreibung.pack()

# out1 im Fenster ausgeben
ausgabe = tk.Label(fenster, textvariable=out, font=('Helvetica',14, 'bold'),
                   bg='light blue', fg='purple', width = 40, height=2)

# ausgabe.grid(row=3,column=0)
ausgabe.pack()

rahmen = tk.Frame(fenster, bg='purple')
rahmen.pack(side='top', padx='10', pady='30')

# Buttons
b1 = tk.Button(rahmen,text='b1', bg='red', highlightbackground='red', fg='black', command=lambda: knopfgedrückt('rot'))
b2 = tk.Button(rahmen, text='b2', bg='green', highlightbackground='green', fg='black', command=lambda: knopfgedrückt('grün'))
b3 = tk.Button(rahmen, text='b2', bg='blue', highlightbackground='blue', fg='black', command=lambda: knopfgedrückt('blau'))

#optionen: after, anchor, before, expand, fill, in, ipadx, ipady, padx, pady, side
b1.pack(side = 'left', padx = 10, pady=40, fill='y')
b2.pack(side = 'left', padx = 10, pady=40, fill='y')
b3.pack(side = 'left', padx = 10, pady=40, fill='y')


# Fenster erzeugen, immer zum Schluss
fenster.mainloop()