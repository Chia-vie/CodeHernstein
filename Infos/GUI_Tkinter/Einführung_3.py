import tkinter as tk

def enterknopf():
    eintrag = eingabe.get()
    out_eingabe.set(eintrag)
    eingabe.delete(0, 'end')
    fenster.update_idletasks()



# ein tkinter fenster erstellen
fenster = tk.Tk()
# Hintergrundfarbe
# Die verschiedenen Farbmöglichkeiten findet man z.B. hier:
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
fenster.config(bg='pale turquoise')

# Name des Fensters
fenster.title('MyCoolApp')

# die Variablen für die Outputs erzeugen und auf einen Startwert setzen
out_eingabe = tk.StringVar()
out_eingabe.set('')

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
beschreibung = tk.Label(fenster, text='Willkommen! Hier kannst du etwas eingeben.', font=('Helvetica', 16, 'bold'),
                        bg='pale turquoise', fg='black', width = 40, height=2)

#beschreibung.grid(row=2,column=0, columnspan=3, rowspan=1)
beschreibung.pack()

# schere.grid(row=3, column=1)

eingabe = tk.Entry(fenster, text='Gib deinen Namen ein!', bd=5)
eingabe.focus()
eingabe.pack()

eingabe_knopf = tk.Button(fenster, text='Enter', font=('Helvetica',10, 'bold'), command=enterknopf)
eingabe_knopf.focus()
eingabe_knopf.pack()

ausgabe_anzeigen = tk.Label(fenster, textvariable=out_eingabe, font=('Helvetica',14, 'bold'),
                   bg='light blue', fg='purple', width = 40, height=2)
ausgabe_anzeigen.pack()


# Fenster erzeugen, immer zum Schluss
fenster.mainloop()