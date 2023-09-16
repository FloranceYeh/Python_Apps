from tkinter import *
from tkinter import messagebox
from random import *

root = Tk()
root.geometry("500x400")

def clicked():
    n = int(spin.get())
    m = int(spin2.get())
    a = list(range(1, n + 1))
    shuffle(a)
    if m >= 6:
        root.geometry("500x450")
        lbl3.grid(column = 0, row = 6)
        lbl2.configure(text = a[:m // 2])
        lbl3.configure(text = a[m // 2:m])
    
    else:
        root.geometry("500x400")
        lbl3.grid(column = 0, row = 5)
        lbl2.configure(text = a[:m])
        lbl3.configure(text='')
    messagebox.showinfo("随机数生成器", "随机数已生成，关闭此窗口查看")

root.title("随机数生成器")

# Title
blank = Label(root, text = "", font = ("Arial Bold", 40))
blank.grid(column = 0, row = 0)
lbl = Label(root, text = "随机生成一些正整数", font = ("Arial Bold", 40))
lbl.grid(column = 0, row = 1)

# Function
btn = Button(root, text="START!", bg = "lightgreen", command = clicked)
btn.grid(column = 0, row = 2)

# Message
lbl2 = Label(root, font = ("Arial Bold", 60))
lbl2.grid(column = 0, row = 5)
lbl3 = Label(root, font = ("Arial Bold", 60))
lbl3.grid(column = 0, row = 5)
copyright = Label(root, text = "Made By Florance", font = ("Arial Bold", 10), fg = "green")
copyright.grid(column = 0, row = 7)

# Options
var = IntVar()
var.set(46)
mess1 = Label(root, text = "                             范围调节", font = ("Arial Bold", 10))
mess1.grid(column = 0, row = 3)
mess2 = Label(root, text = "                             个数调节", font = ("Arial Bold", 10))
mess2.grid(column = 0, row = 4)
spin = Spinbox(root, from_ = 0, to = 1000, width = 5, textvariable = var)
spin.grid(column = 0, row = 3)
spin2 = Spinbox(root, from_ = 1, to = 100, width = 5)
spin2.grid(column = 0, row = 4)

root.mainloop()