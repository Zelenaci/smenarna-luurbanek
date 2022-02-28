import tkinter
from tkinter import * 

 
okno = Tk() 
v = IntVar() 
 
Radiobutton(okno, text="Nákup", variable=v, value=1).grid(row=0, column=0)
Radiobutton(okno, text="Prodej", variable=v, value=2).grid(row=0, column=1)


listbox = Listbox(okno)
listbox.grid(row=1, column=0, columnspan=2)

listbox.insert(END, u"položka seznamu")
for item in [u"Euro", u"Koruna", u"Rubl", u"Dolar"]:
    listbox.insert(END, item)
 

vstup = Entry(okno)
vstup.grid(row=2, column=0, columnspan=2)

mainloop()