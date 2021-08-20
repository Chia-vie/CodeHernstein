import tkinter as tk

fenster = tk.Tk()

eb = 50
rechtecke = [[0,0,eb,eb],[eb,0,2*eb,eb],[2*eb,0,3*eb,eb]]

feld = tk.Canvas(fenster, width=500, height=500, bg = 'grey')
feld.pack()

for element in rechtecke:
    feld.create_rectangle(element, fill='blue')

fenster.bind('<KeyPress-Right>', lambda e: right())

def right():
    kopf = rechtecke[-1]
    rechtecke.pop(0)
    neux0 = kopf[0]+eb
    neuy0 = kopf[1]
    neux1 = kopf[2]+eb
    neuy1 = kopf[3]
    neuerkopf = [neux0,neuy0,neux1,neuy1]
    rechtecke.append(neuerkopf)
    feld.delete('all')
    for element in rechtecke:
        feld.create_rectangle(element, fill='blue')

fenster.mainloop()