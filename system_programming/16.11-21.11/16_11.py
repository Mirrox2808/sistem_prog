from tkinter import *
from tkinter import messagebox

root = Tk()

num = Entry(width=15)
num2 = Entry(width=15)
but_plus = Button(text="+", width=17)
but_minus = Button(text="-", width=17)
but_multi = Button(text="*", width=17)
but_div = Button(text="/", width=17)
lab = Label(width=20)


def plus(event):
    g = num.get()
    g2 = num2.get()
    try:
        dm = (str(g))
        dm1 = (str(g2))
        dm2 = (float(g))
        dm3 = (float(g2))
        result = dm2 + dm3
        z = (str(result))
        lab['text'] = z
    except ValueError:
        messagebox.showerror("Ошибка","Введите корректные значения")


def minus(event):
    a = num.get()
    aa = num2.get()
    try:
        m = (str(a))
        m1 = (str(aa))
        m2 = (float(a))
        m3 = (float(aa))
        result = m2 - m3
        b = (str(result))
        lab['text'] = b
    except ValueError:
        messagebox.showerror("Ошибка","Введите корректные значения")


def multi(event):
    c = num.get()
    c1 = num2.get()
    try:
        y = (str(c))
        y1 = (str(c1))
        y2 = (float(c))
        y3 = (float(c1))
        result = y2 * y3
        x = (str(result))
        lab['text'] = x
    except ValueError:
        messagebox.showerror("Ошибка","Введите корректные значения")


def div(event):
    p = num.get()
    p1 = num2.get()
    try:
        o = (str(p))
        o1 = (str(p1))
        o2 = (float(p))
        o3 = (float(p1))
        result = o2 / o3
        l = (str(result))
        lab['text'] = l
    except ValueError:
        messagebox.showerror("Ошибка","Введите корректные значения")


but_plus.bind('<Button-1>', plus)
but_minus.bind('<Button-1>', minus)
but_multi.bind('<Button-1>', multi)
but_div.bind('<Button-1>', div)


num.pack()
num2.pack()
but_plus.pack()
but_minus.pack()
but_multi.pack()
but_div.pack()
lab.pack()
root.mainloop()