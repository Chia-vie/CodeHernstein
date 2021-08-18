import tkinter as tk

def knopfgedrückt(text):
    global out
    print('In der App wurde gerade ein Knopf gedrückt')
    # die verschiedenen outputs einer Variable zuordnen
    out.set(f'Hihi! {text} hat mich gedrückt!')
    fenster.update_idletasks()

# ein tkinter fenster erstellen
fenster = tk.Tk()
# Hintergrundfarbe
# Die verschiedenen Farbmöglichkeiten findet man z.B. hier:
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
fenster.config(bg='pale turquoise')

# Name des Fensters
fenster.title('MyCoolApp')

# die Variablen für die Outputs erzeugen und auf '' = nichts setzen
out = tk.StringVar()
out.set('Drück den Knopf!')

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
beschreibung = tk.Label(fenster, text='Willkommen! Hier kannst du einen Knopf drücken!', font=('Helvetica', 16, 'bold'),
                        bg='pale turquoise', fg='black', width = 40, height=2)

#beschreibung.grid(row=2,column=0, columnspan=3, rowspan=1)
beschreibung.pack()

# out1 im Fenster ausgeben
ausgabe = tk.Label(fenster, textvariable=out, font=('Helvetica',14, 'bold'),
                   bg='light blue', fg='purple', width = 40, height=2)

#ausgabe.grid(row=3,column=0)
ausgabe.pack()

# Schere, Stein, Papier Knöpfe
knopf = tk.Button(fenster, text='Ich bin ein Knopf!', font=('Helvetica',14, 'bold'),
                  fg='blue4', width=40, height=10, command=lambda: knopfgedrückt('Chrisi'))

# schere.grid(row=3, column=1)
knopf.pack()

# Fenster erzeugen, immer zum Schluss
fenster.mainloop()