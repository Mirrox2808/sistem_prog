from tkinter import *


def OpFile():
    f1=open(text2.get())
    text.delete(1.0, END)
    text.insert(1.0, f1.read())


def SvFile():
    f1 = open(text2.get(), 'x')
    f1.write(text.get(1.0, END))
    text.delete(1.0, END)


root = Tk()
f = Frame()
f.pack()
text2 = Entry(f, width=20)
text2.pack()

Button(f, text="Открыть", command=OpFile)\
    .pack(side=LEFT)
Button(f, text="Сохранить", command=SvFile)\
    .pack(side=LEFT)

f2 = Frame()
f2.pack()
text = Text(f2, width=50, height=20, wrap=NONE)
text.pack(side=LEFT)

scroll = Scrollbar(f2, command=text.yview)
scroll.pack(side=LEFT, fill=Y)
text.config(yscrollcommand=scroll.set)

scroll2 = Scrollbar(orient=HORIZONTAL, command=text.xview)
scroll2.pack(side=BOTTOM, fill=X)
text.config(xscrollcommand=scroll2.set)

root.mainloop()