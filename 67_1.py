import tkinter
from random import *
canvas = tkinter.Canvas()
canvas.pack()


def klik(event):
    x=event.x
    y=event.y
    meno=entry1.get()
    canvas.create_rectangle(x,y,x+20,y+20)
    canvas.create_oval(x,y,x+20,y-20)
    canvas.create_text(x-5,y+20,text=meno,anchor='nw')



entry1 = tkinter.Entry()
entry1.pack()
canvas.bind('<Button-1>', klik)


