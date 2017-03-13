from tkinter import *

root = Tk()

var = StringVar()
label = Label(root, textvariable=var, relief=FLAT)
e = Entry(root)
cenepe = e.get()
e.pack()
var.set("Introdu CNP")
label.pack()
#from amihaita.cacat.Python.cnp import verifica
buton = Button(root, text="Verifică")
buton.pack()

text = Text(root)
text.insert(INSERT, cenepe)
text.pack()
root.mainloop()