import tkinter as tk
app = tk.Tk()
app.geometry("1920x1080")
app.title("Clicker Game")

#def knopfgedrückt(text):
    #global out
    # die verschiedenen outputs einer Variable zuordnen
    #out.set
    #app.update_idletasks()


#beschreibung = tk.Label(app, text='Willkommen! Hier kannst du einen Knopf drücken!', font=('Helvetica', 16, 'bold'),
                        #bg='pale turquoise', fg='black', width = 40, height=2)

header = tk.Label(app,text='Clicker Game',
                        font=('Gothic',24, 'bold'), bg='gray1', fg='red2', width = 40, height=2)
header.pack()
app.config(bg='gray1')


#out = tk.StringVar()
#out.set('Drück den Knopf!')

#rahmen = tk.Frame(app, bg='purple')
#rahmen.pack(side='top', padx='10', pady='30')
#knopf = tk.Button(app, text='0', font=('Gothic',20, 'bold'),
                  #fg='blue4', width=20, height=5, command=lambda: knopfgedrückt('Chrisi'))



#knopf.pack()




counter = tk.IntVar()

def onClick(event=None):
    counter.set(counter.get() + 1)

tk.Label(app, textvariable=counter, width=200, height=5, fg="gray100", bg = "gray1").pack()
tk.Button(app, text="Click for Point", command=onClick, activeforeground="green2", fg="green2", activebackground = "gray1", bg = "gray1", width=10000, height=10000).pack()




class Fullscreen_Example:
    def __init__(self):
        self.window = tk.Tk()
        self.window.attributes('-fullscreen', True)
        self.fullScreenState = False
        self.window.bind("<F11>", self.toggleFullScreen)
        self.window.bind("<Escape>", self.quitFullScreen)

        self.window.mainloop()

    def toggleFullScreen(self, event):
        self.fullScreenState = not self.fullScreenState
        self.window.attributes("-fullscreen", self.fullScreenState)

    def quitFullScreen(self, event):
        self.fullScreenState = False
        self.window.attributes("-fullscreen", self.fullScreenState)

if __name__ == '__main__':
    app = Fullscreen_Example()



app.mainloop()
