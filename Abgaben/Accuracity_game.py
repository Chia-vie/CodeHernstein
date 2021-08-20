import tkinter as tk
fenster = tk.Tk()
fenster.config(bg = 'royalblue')
fenster.title('Dynamische Objekte in tkinter')






fenster.geometry("1920x1080")
feld = tk.Canvas(fenster, width=1920, height=1080, bd=0, bg='pale turquoise')
feld.delete("all")













fenster.mainloop()
