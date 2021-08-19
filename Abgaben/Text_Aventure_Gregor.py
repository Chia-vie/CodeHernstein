import tkinter as tk
import time

def enterknopf_start():
    eintrag = eingabe.get()
    if eintrag.upper() == 'JA':
        loslegen.set('Dann lass uns loslegen!')
        Bruecke.set('Eine Alte kappute Brücke!')
        Bruecke_entscheidung.set('Willst du über die Brücke gehen?')
    else:
        loslegen.set('Du Feigling!')
        Bruecke_entscheidung.set('Du Feigling!')
    eingabe.delete(0, 'end')
    fenster.update_idletasks()

def enterknopf_bruecke():
    eintrag = eingabe_bruecke.get()
    if eintrag.upper() == 'JA':
        Bruecke_gehen.set('Huch! Es war ein schwieriger Weg aber ich habe es geschaft!')
        Berg_gehen_entscheidung.set('Willst du den Berg besteigen?')
    else:
        Bruecke_gehen.set('Du Feigling!')
    eingabe_bruecke.delete(0, 'end')
    fenster.update_idletasks()

def enterknopf_berg():
    eintrag = eingabe_berg.get()
    if eintrag.upper() == 'JA':
        Berg_gehen.set('Ahhh! Das war so anstremgend! Ich sterbe!')
    else:
        Berg_gehen.set('Ich suche einen Umweg!')
        Baeren_Wald_entscheidung.set('Soll ich durch den gefährlichen Bären Wald gehen, denn dieser Weg spart mir drei Tage!\n')
    eingabe_berg.delete(0, 'end')
    fenster.update_idletasks()

def enterknopf_baeren_wald():
    eintrag = eingabe_baeren_wald.get()
    if eintrag.upper() == 'JA':
        Dorf_finden.set('HUURAAA! Ich hab das Dorf gefunden!')
    else:
        Baeren_Wald_gehen('Ahhh ich habe kein Wasser ich verdurste!')
    eingabe_baeren_wald.delete(0, 'end')
    fenster.update_idletasks()

# ein tkinter fenster erstellen
fenster = tk.Tk()

fenster.config(bg='black') # Hintergrundfarbe des Fensters

fenster.geometry('1000x1000') # Format des Fensters

fenster.title('Dunkle Reise') # Name des Fensters

ueberschrift = tk.Label(fenster, text='||| DARK RISE |||',
                        font=('Helvetica',24, 'bold'), bg='black', fg='red', width = 20, height=2)
ueberschrift.pack(side='top')

beschreibung = tk.Label(fenster, text='Willkommen! Zur Dunklen Reise!', font=('Helvetica', 16, 'bold'),
                        bg='black', fg='red', width = 40, height=2)
beschreibung.pack()

anfang = tk.Label(fenster, text='Bist du Bereit?!', font=('Helvetica', 16, 'bold'),
                        bg='black', fg='red', width = 40, height=2)
anfang.pack()


'''out_eingabe = tk.StringVar()
out_eingabe.set('')'''
loslegen = tk.StringVar()
loslegen.set('')
Bruecke = tk.StringVar()
Bruecke.set('')
Bruecke_gehen = tk.StringVar()
Bruecke_gehen.set('')
Bruecke_entscheidung = tk.StringVar()
Bruecke_entscheidung.set('')
Berg_gehen = tk.StringVar()
Berg_gehen.set('')
Berg_gehen_entscheidung = tk.StringVar()
Berg_gehen_entscheidung.set('')
Baeren_Wald_entscheidung = tk.StringVar()
Baeren_Wald_entscheidung.set('')
Dorf_finden = tk.StringVar()
Dorf_finden.set('')



eingabe = tk.Entry(fenster, text='Bist du Bereit?! (Bitte in Großbuchstaben schreiben!)', bd=5)

eingabe.focus()
eingabe.pack()


eingabe_knopf = tk.Button(fenster, text='Enter', font=('Helvetica',10, 'bold'), command=enterknopf_start)
eingabe_knopf.focus()
eingabe_knopf.pack()

Loslegen = tk.Label(fenster, textvariable=loslegen, font=('Helvetica',16, 'bold'),
                   bg='black', fg='red', width = 40, height=2)
Loslegen.pack()


bruecke = tk.Label(fenster, textvariable=Bruecke, font=('Helvetica', 16, 'bold'),
                    bg='black', fg='red', width = 40, height=2)
bruecke.pack()

bruecke_entscheidung = tk.Label(fenster, textvariable=Bruecke_entscheidung, font=('Helvetica', 16, 'bold'),
                    bg='black', fg='red', width = 40, height=2)

bruecke_entscheidung.pack()

eingabe_bruecke = tk.Entry(fenster, bd=5)

eingabe_bruecke.pack()


eingabe_knopf = tk.Button(fenster, text='Enter', font=('Helvetica',10, 'bold'), command=enterknopf_bruecke)

eingabe_knopf.focus()
eingabe_knopf.pack()

bruecke_gehen = tk.Label(fenster, textvariable=Bruecke_gehen, font=('Helvetica', 16, 'bold'),
                    bg='black', fg='red', width = 60, height=2)

bruecke_gehen.pack()

berg_gehen_entscheidung = tk.Label(fenster, textvariable=Berg_gehen_entscheidung, font=('Helvetica', 16, 'bold'),
                    bg='black', fg='red', width = 60, height=2)

berg_gehen_entscheidung.pack()




eingabe_berg = tk.Entry(fenster, bd=5)

eingabe_berg.pack()


eingabe_knopf_berg = tk.Button(fenster, text='Enter', font=('Helvetica',10, 'bold'), command=enterknopf_berg)

eingabe_knopf_berg.focus()
eingabe_knopf_berg.pack()

berg_gehen = tk.Label(fenster, textvariable=Berg_gehen, font=('Helvetica', 16, 'bold'),
                    bg='black', fg='red', width = 60, height=2)

berg_gehen.pack()

baren_wald_entscheidung = tk.Label(fenster, textvariable=Baeren_Wald_entscheidung, font=('Helvetica', 16, 'bold'),
                    bg='black', fg='red', width = 100, height=2)

baren_wald_entscheidung.pack()

eingabe_baeren_wald = tk.Entry(fenster, bd=5)

eingabe_baeren_wald.pack()

eingabe_knopf_baeren_wald = tk.Button(fenster, text='Enter', font=('Helvetica',10, 'bold'), command=enterknopf_baeren_wald)

eingabe_knopf_baeren_wald.focus()
eingabe_knopf_baeren_wald.pack()

dorf_finden = tk.Label(fenster, textvariable=Dorf_finden, font=('Helvetica', 16, 'bold'),
                    bg='black', fg='red', width = 60, height=2)

dorf_finden.pack()






fenster.mainloop()
