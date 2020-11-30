from tkinter import *


def red():
    e1.delete(0, END)
    e1.insert(0, "#ff0000")
    l1['text'] = "красный"


def oren():
    e1.delete(0,END)
    e1.insert(0, "#ff7d00")
    l1['text'] = "оранжевый"


def yell():
    e1.delete(0, END)
    e1.insert(0, "#ffff00")
    l1['text'] = "желтый"


def gre():
    e1.delete(0, END)
    e1.insert(0, "#00ff00")
    l1['text'] = "зеленый"


def bl():
    e1.delete(0, END)
    e1.insert(0, "#007dff")
    l1['text'] = "голубой"


def b():
    e1.delete(0, END)
    e1.insert(0, "#0000ff")
    l1['text'] = "синий"


def pur():
    e1.delete(0, END)
    e1.insert(0, "#7d00ff")
    l1['text'] = "фиолетовый"


root = Tk()
l1 = Label()
e1 = Entry(width=20, justify=CENTER)
b1 = Button(width=3, height=1, bg='#ff0000')
b2 = Button(width=3, height=1, bg='#ff7d00')
b3 = Button(width=3, height=1, bg='#ffff00')
b4 = Button(width=3, height=1, bg='#00ff00')
b5 = Button(width=3, height=1, bg='#007dff')
b6 = Button(width=3, height=1, bg='#0000ff')
b7 = Button(width=3, height=1, bg='#7d00ff')
b1.config(command=red)
b2.config(command=oren)
b3.config(command=yell)
b4.config(command=gre)
b5.config(command=bl)
b6.config(command=b)
b7.config(command=pur)
l1.pack(expand=1)
e1.pack()
b1.pack(side=LEFT, padx=1, pady=10)
b2.pack(side=LEFT, padx=1, pady=10)
b3.pack(side=LEFT, padx=1, pady=10)
b4.pack(side=LEFT, padx=1, pady=10)
b5.pack(side=LEFT, padx=1, pady=10)
b6.pack(side=LEFT, padx=1, pady=10)
b7.pack(side=LEFT, padx=1, pady=10)
root.mainloop()