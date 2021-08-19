import tkinter as tk

def update_spielzuege(spielzug, button_gedr):
    global symbol, winner_text, kreuz, kreis
    spielzuege[int(spielzug)-1] = symbol

    print(spielzuege)

    if (spielzuege[0] == spielzuege[1] == spielzuege[2] or
    spielzuege[3] == spielzuege[4] == spielzuege[5] or
    spielzuege[6] == spielzuege[7] == spielzuege[8] or
    spielzuege[0] == spielzuege[3] == spielzuege[6] or
    spielzuege[1] == spielzuege[4] == spielzuege[7] or
    spielzuege[2] == spielzuege[5] == spielzuege[8] or
    spielzuege[0] == spielzuege[4] == spielzuege[8] or
    spielzuege[2] == spielzuege[4] == spielzuege[6]):

        winner_text.set(f"Spieler {symbol}, du hast gewonnen!")
        # Update App
        app.update_idletasks()
        #quit()

    if symbol == 'X':
        button_gedr.update(image=kreuz)
        symbol = 'O'
    else:
        button_gedr.update(image=kreis)
        symbol = 'X'
    app.update_idletasks()

    if all(x in ["X", "0"] for x in spielzuege):
        quit()

app = tk.Tk()

kreuz = tk.PhotoImage('kreuz_klein.png')
kreis = tk.PhotoImage('kreis.png')
leer = tk.PhotoImage('leer.png')

# Var define
# Die Zahlen werden im Lauf des Spiels durch X oder O ersetzt.
spielzuege = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = 'X'
winner_text = tk.StringVar()
winner_text.set('Tic Tac Toe')



# Basic App-Fenster Einstellungen
app.config(bg="white")
app.title("Tic Tac Toe")

# Basic App-Fenster Design
# Überschrift



ueberschrift = tk.Label(app, textvariable=winner_text,
                        font=('Helvetica',24, 'bold'), bg='white',
                        fg='black')#, width=100, height=2)

ueberschrift.pack()#row=0, column=0, columnspan=3, rowspan=1)
# Positionen
# row,column
#  __ __ __
# |00 01 02|
# |10 11 12|
# |20 21 22|

# Button1
knopf1 = tk.Button(app, image=leer, font=("Helvetica", 40, "bold"), bg="white",
                  fg="black", width=4, height=1, command=lambda: update_spielzuege("1", knopf1))
#knopf.grid(row=1, column=0, columnspan=1, rowspan=1)
knopf1.place(x=0, y=0, width=100, height=100)

#  __ __ __
# |00 01 02|
# |10 11 12|
# |20 21 22|

# Button2
knopf2 = tk.Button(app, image=kreuz, font=("Helvetica", 40, "bold"), bg="white",
                  fg="black", width=4, height=1, command=lambda: update_spielzuege("2", knopf2))
#knopf.grid(row=1, column=1, columnspan=1, rowspan=1)
knopf2.place(x=100, y=0, width=100, height=100)


# Button3
knopf3 = tk.Button(app, image=leer, font=("Helvetica", 40, "bold"), bg="white",
                  fg="black", width=4, height=1, command=lambda: update_spielzuege("3", knopf3))
#knopf.grid(row=1, column=2, columnspan=1, rowspan=1)
knopf3.place(x=200, y=0, width=100, height=100)


# Button4
knopf4 = tk.Button(app, image=leer, font=("Helvetica", 40, "bold"), bg="white",
                  fg="black", width=4, height=1, command=lambda: update_spielzuege("4", knopf4))
#knopf.grid(row=2, column=0, columnspan=1, rowspan=1)
knopf4.place(x=0, y=100, width=100, height=100)


# Button5
knopf5 = tk.Button(app, image=leer, font=("Helvetica", 40, "bold"), bg="white",
                  fg="black", width=4, height=1, command=lambda: update_spielzuege("5", knopf5))
#knopf.grid(row=2, column=1, columnspan=1, rowspan=1)
knopf5.place(x=100, y=100, width=100, height=100)


# Button6
knopf6 = tk.Button(app, image=leer, font=("Helvetica", 40, "bold"), bg="white",
                  fg="black", width=4, height=1, command=lambda: update_spielzuege("6", knopf6))
#knopf.grid(row=2, column=2, columnspan=1, rowspan=1)
knopf6.place(x=200, y=100, width=100, height=100)


# Button7
knopf7 = tk.Button(app, image=leer, font=("Helvetica", 40, "bold"), bg="white",
                  fg="black", width=4, height=1, command=lambda: update_spielzuege("7", knopf7))
#knopf.grid(row=3, column=0, columnspan=1, rowspan=1)
knopf7.place(x=0, y=200, width=100, height=100)


# Button8
knopf8 = tk.Button(app, image=leer, font=("Helvetica", 40, "bold"), bg="white",
                  fg="black", width=4, height=1, command=lambda: update_spielzuege("8", knopf8))
#knopf.grid(row=3, column=1, columnspan=1, rowspan=1)
knopf8.place(x=100, y=200, width=100, height=100)


# Button9
knopf9 = tk.Button(app, image=leer, font=("Helvetica", 40, "bold"), bg="white",
                  fg="black", width=4, height=1, command=lambda: update_spielzuege("9", knopf9))
#knopf.grid(row=3, column=2, columnspan=1, rowspan=1)
knopf9.place(x=200, y=200, width=100, height=100)



# Update App
app.update_idletasks()






# Run App
app.mainloop()
