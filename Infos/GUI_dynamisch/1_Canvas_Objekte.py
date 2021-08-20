import tkinter as tk

fenster = tk.Tk()

fenster.config(bg = 'royalblue')
fenster.title('Canvas Objekte in tkinter')

feldbreite = 1000
feldhoehe = 1000

feld = tk.Canvas(fenster, width=feldbreite, height=feldhoehe, bd=0, bg='pale turquoise')
feld.pack()

rechteck1 = feld.create_rectangle(50, 50, 150, 200, fill = "royal blue")
feld.move(rechteck1, 0, 0)


rechteck2 = feld.create_rectangle(150, 50, 250, 200, fill = "red")
feld.move(rechteck2, 0, 0)


oval1 = feld.create_oval(250, 50, 350, 200, fill = "blue")
feld.move(oval1, 0, 0)

oval2 = feld.create_oval(350, 50, 450, 200, fill = "purple")
feld.move(oval2, 0, 0)

# Sternchen - Punkte
points = [0, 50, 40, 40, 50, 0, 60, 40, 100, 50, 60, 60, 50, 100, 40, 60]
'''

           x


         x    x
x                     x
         x    x


           x

'''

sternchen = feld.create_polygon(points, fill='royal blue')
feld.move(sternchen, feldbreite/2 - 50, feldhoehe/2 - 50)

colors=["white", "black", "red", "green", "blue", "cyan", "yellow", "magenta","grey", "brown"]

kreisbreite = feldbreite/10
for i in range(10):
    oval = feld.create_oval(kreisbreite*i+5, 300, kreisbreite*i+kreisbreite, 400, fill=colors[i])
    feld.move(oval,0,0)


boden = feld.create_line(0,400,feldbreite,400, fill='green', width=5)

for i in range(int(feldbreite/2)):
    line = feld.create_line(i*2,400,i*2,390, fill='dark green',width=1)

schrift = feld.create_text(feldbreite/2, feldhoehe/2, text="HUHU!", font=('Helvetica',24, 'bold'))

fenster.mainloop()