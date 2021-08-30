import tkinter as tk
from rechner_functions2 import Rechner
class Eingeben:
    def __init__(self):
        num1 = ""
        output1 = 0
        self.num1 = num1
        self.output1 = output1
        global var1

    def buttonpress(self, number):
        if number == "-":
            avar = "-"
            avar += self.num1
            self.num1 = avar
        else:
            self.num1 = str(self.num1)
            self.num1 += str(number)
        var1.set(self.num1)

    def rechenoperation(self, operation):
        self.output1 = float(self.num1)
        self.num1 = ""
        self.operation = operation

    def equals(self):
        self.num1 = float(self.num1)
        calc = Rechner(self.output1, self.num1)
        exp = 0
        if self.operation == "addieren":
            exp = calc.addieren()
        if self.operation == "subtrahieren":
            exp = calc.subtrahieren()
        if self.operation == "multiplitzieren":
            exp = calc.multiplitzieren()
        if self.operation == "dividieren":
            if self.num1 == 0:
                exp = "Not possible!"
            else:
                exp = calc.dividieren()
        if self.operation == "potenzieren":
            exp = calc.potenzieren()
        if self.operation == "wurzel":
            if self.output1 < 0:
                exp = "Not possible!"
            else:
                exp = calc.wurzel()
        var1.set(exp)
        self.num1 = 0
        self.output1 = 0
    def reset(self):
        self.num1 = ""
        self.output1 = 0
        var1.set("0")
rechner = tk.Tk()
rechner.title('Taschenrechner')
rechner.geometry('589x746')
var1 = tk.StringVar()
var1.set("0")
eing = Eingeben()
eingabe = tk.Label(rechner, textvariable=var1, font=('calibri', 30, 'bold'), fg='black', width='25', height='3')
taste1 = tk.Button(rechner, text='1', font=('calibri', 13, 'bold'), bg='ghost white', fg='black', width='15', height='5', command=lambda: eing.buttonpress(1))
taste2 = tk.Button(rechner, text='2', font=('calibri', 13, 'bold'), bg='ghost white', fg='black', width='15', height='5', command=lambda: eing.buttonpress(2))
taste3 = tk.Button(rechner, text='3', font=('calibri', 13, 'bold'), bg='ghost white', fg='black', width='15', height='5', command=lambda: eing.buttonpress(3))
taste4 = tk.Button(rechner, text='4', font=('calibri', 13, 'bold'), bg='ghost white', fg='black', width='15', height='5', command=lambda: eing.buttonpress(4))
taste5 = tk.Button(rechner, text='5', font=('calibri', 13, 'bold'), bg='ghost white', fg='black', width='15', height='5', command=lambda: eing.buttonpress(5))
taste6 = tk.Button(rechner, text='6', font=('calibri', 13, 'bold'), bg='ghost white', fg='black', width='15', height='5', command=lambda: eing.buttonpress(6))
taste7 = tk.Button(rechner, text='7', font=('calibri', 13, 'bold'), bg='ghost white', fg='black', width='15', height='5', command=lambda: eing.buttonpress(7))
taste8 = tk.Button(rechner, text='8', font=('calibri', 13, 'bold'), bg='ghost white', fg='black', width='15', height='5', command=lambda: eing.buttonpress(8))
taste9 = tk.Button(rechner, text='9', font=('calibri', 13, 'bold'), bg='ghost white', fg='black', width='15', height='5', command=lambda: eing.buttonpress(9))
taste0 = tk.Button(rechner, text='0', font=('calibri', 13, 'bold'), bg='ghost white', fg='black', width='15', height='5', command=lambda: eing.buttonpress(0))
taste_negate = tk.Button(rechner, text='+/-', font=('calibri', 13, 'bold'), bg='ghost white', fg='black', width='15', height='5', command=lambda: eing.buttonpress("-"))
taste_comma = tk.Button(rechner, text='.', font=('calibri', 13, 'bold'), bg='ghost white', fg='black', width='15', height='5', command=lambda: eing.buttonpress("."))
taste_equals = tk.Button(rechner, text='=', font=('calibri', 13, 'bold'), bg='steel blue', fg='black', width='16', height='5', command=lambda: eing.equals())
taste_plus = tk.Button(rechner, text='+', font=('calibri', 13, 'bold'), bg='light steel blue', fg='black', width='16', height='5', command=lambda: eing.rechenoperation("addieren"))
taste_minus = tk.Button(rechner, text='-', font=('calibri', 13, 'bold'), bg='light steel blue', fg='black', width='16', height='5', command=lambda: eing.rechenoperation("subtrahieren"))
taste_times = tk.Button(rechner, text='*', font=('calibri', 13, 'bold'), bg='light steel blue', fg='black', width='16', height='5', command=lambda: eing.rechenoperation("multiplitzieren"))
taste_division = tk.Button(rechner, text='/', font=('calibri', 13, 'bold'), bg='light steel blue', fg='black', width='16', height='5', command=lambda: eing.rechenoperation("dividieren"))
taste_clear = tk.Button(rechner, text='C', font=('calibri', 13, 'bold'), bg='ghost white', fg='black', width='15', height='5', command=lambda: eing.reset())
taste_power = tk.Button(rechner, text='^', font=('calibri', 13, 'bold'), bg='ghost white', fg='black', width='15', height='5', command=lambda: eing.rechenoperation("potenzieren"))
taste_root = tk.Button(rechner, text='√', font=('calibri', 13, 'bold'), bg='ghost white', fg='black', width='15', height='5', command=lambda: eing.rechenoperation("wurzel"))
taste_negate.grid(row=6, column=0)
taste0.grid(row=6, column=2)
taste_comma.grid(row=6, column=3)
taste_equals.grid(row=6, column=4)
taste1.grid(row=5, column=0)
taste2.grid(row=5, column=2)
taste3.grid(row=5, column=3)
taste_plus.grid(row=5, column=4)
taste4.grid(row=4, column=0)
taste5.grid(row=4, column=2)
taste6.grid(row=4, column=3)
taste_minus.grid(row=4, column=4)
taste7.grid(row=3, column=0)
taste8.grid(row=3, column=2)
taste9.grid(row=3, column=3)
taste_times.grid(row=3, column=4)
taste_division.grid(row=2, column=4)
taste_clear.grid(row=2, column=3)
taste_root.grid(row=2, column=2)
taste_power.grid(row=2, column=0)
eingabe.grid(row=0, column=0, columnspan=5)
rechner.mainloop()

