import tkinter,random
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(50,50,100,200,fill='black')
def kresli():
    canvas.delete('farba')
    cislo=random.randrange(1,4)
    if cislo==1:
        canvas.create_oval(50,50,100,80,fill='red',tag='farba')
        canvas.create_oval(50,90,100,120,fill='yellow',tag='farba')
        canvas.create_oval(50,130,100,160,fill='green',tag='farba')
    if cislo==2:
        canvas.create_oval(50,50,100,80,fill='red',tag='farba')
        canvas.create_oval(50,90,100,120,fill='yellow',tag='farba')
    if cislo==3:
        cislo1=random.randrange(3)
        if cislo1==1:
            canvas.create_oval(50,50,100,80,fill='red',tag='farba')
        if cislo1==0:   
            canvas.create_oval(50,90,100,120,fill='yellow',tag='farba')
        else:
            canvas.create_oval(50,130,100,160,fill='green',tag='farba')
    canvas.after(250,kresli)
kresli()
