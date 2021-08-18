import tkinter as tk

# ein tkinter fenster erstellen
fenster = tk.Tk()


# Hintergrundfarbe
# Die verschiedenen Farbmöglichkeiten findet man z.B. hier:
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
fenster.config(bg='pale turquoise')

#fenster größe
fenster.geometry('1000x1000')

# Name des Fensters
fenster.title('MyCoolApp')


# Überschrift im Fenster
ueberschrift = tk.Label(fenster, text='*******    Meine coole App    ********',
                        font=('Helvetica',24, 'bold'), bg='black', fg='red', width = 40, height=10)

#ueberschrift.grid(row=0, column=0, columnspan=3, rowspan=2)
# Positionen
# row,column
#  __ __ __
# |00 01 02|
# |10 11 12|
# |20 21 22|
ueberschrift.pack(side='top')

# Text im Fenster
beschreibung = tk.Label(fenster, text='Willkommen! Hier kannst du nichts machen.', font=('Helvetica', 16), bg='light blue', fg='black')

# ACHTUNG: .grid und .pack können nicht in der gleichen App verwendet werden
beschreibung.place(x = 20, y = 30, width=350, height=25)
#beschreibung.grid(row=2,column=0, columnspan=3, rowspan=1)
#beschreibung.pack()

# Fenster erzeugen
fenster.mainloop()