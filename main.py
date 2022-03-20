from os.path import basename, splitext
import tkinter as tk
import random
from tkinter import *

class About(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent, class_=parent.name)
        self.config()

class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Smenarna"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.lbl = tk.Label(self, text="Směnárna", bg="#FFFFFF", font=("Arial", 30, "underline"))
        self.lbl.grid(row=0, column=0, padx=20)
        self.geometry("225x600")
        self.configure(bg='#87CEFA')

        #nakoupit nebo prodat
        self.variable = tk.IntVar(self)
        self.radiobutton1 = Radiobutton(self, text="Chci nakoupit", bg="#FAAFBA", font=("Arial", 15), variable=self.variable, value=1).grid(row=1, column=0)
        self.radiobutton2 = Radiobutton(self, text="Chci prodat", bg="#FAAFBA", font=("Arial", 15), variable=self.variable, value=2).grid(row=2, column=0)
        self.variable.set(1)

        #meny
        self.lbl2 = tk.Label(self, text="Nabídka měn", font=("Arial", 15), bg="#FFFFFF")
        self.lbl2.grid(row=3, column=0)
        self.listbox = tk.Listbox(self)
        self.listbox.grid(row=4, column=0)
        self.listbox.bind("<ButtonRelease-1>", self.kliknuti)       
        f = open('listek.txt', 'r')
        slovnik = {}
        for line in f:
            self.listbox.insert(tk.END,line.split()[0])
            slovnik[line.split()[0]] = (line.split()[1:])

        #kurz meny
        self.lbl3 = tk.Label(self, text="Kurz", font=("Arial", 15), bg="#FFFFCC")
        self.lbl3.grid(row=5, column=0)
        self.hodnota = tk.StringVar()
        self.cena = tk.IntVar()
        self.cenaLbl= tk.Label(self, textvariable=self.cena, bg="#FFFFCC", font=("Arial", 15)) 
        self.cenaLbl.grid(row=6, column=0)
        self.hodnotal= tk.Label(self, textvariable= self.hodnota, bg="#FFFFCC", font=("Arial", 15)) 
        self.hodnotal.grid(row=7, column=0)

        #vypocitat
        self.lbl2 = tk.Label(self, text="Kolik:", font=("Arial", 15), bg="#FFFFFF")
        self.lbl2.grid(row=8, column=0)
        self.mnozstvi = tk.Entry(self, font=("Arial", 15))
        self.mnozstvi.grid(row=9, column=0)
        self.btn2 = tk.Button(self, text="Vypočítej", font=("Arial", 15), command=self.vypocet, bg="#ffffff")
        self.btn2.grid(row=10, column=0)
        self.vysledek = tk.IntVar()
        self.vysledekl= tk.Label(self, textvariable= self.vysledek, bg="#ffffff", font=("Arial", 15))
        self.vysledekl.grid(row=11, column=0)
        self.lbl4 = tk.Label(self, bg="#87CEFA", font=("Arial", 15))
        self.lbl4.grid(row=12, column=0)
        

        #zavrit
        self.bind("<Escape>", self.quit)
        self.btn1 = tk.Button(self, text="Zavřít", font=("Arial", 15), command=self.quit, bg="#ffffff")
        self.btn1.grid(row=13, column=0)

    
    def vypocet(self,event=None):

        a = int(self.mnozstvi.get())
        b = int(self.cena.get())
        c = float(self.hodnota.get().replace(",","."))
        self.vysledekVar = float(a*c/b)
        self.vysledek.set(self.vysledekVar)

    def kliknuti(self, event):
        index = self.listbox.curselection()[0]
        f = open("listek.txt")
        self.lines = f.readlines()
        self.cenaVar = self.lines[index].split()[1]
        self.cena.set(self.cenaVar)
        if self.variable.get() == 1: 
            self.hodnotaVar = self.lines[index].split()[3] 
        else:
            self.hodnotaVar = self.lines[index].split()[2] 
        self.hodnota.set(self.hodnotaVar)

    def quit(self, event=None):
        super().quit()

app = Application()
app.mainloop()