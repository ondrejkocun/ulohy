import tkinter,random
canvas = tkinter.Canvas()
canvas.pack()

canvas.create_rectangle(50,100,150,200,fill='red')
canvas.create_rectangle(200,100,300,200,fill='green')
body=0
def hocico():
    global cislo1,cislo2
    cislo1=random.randrange(1,7)
    cislo2=random.randrange(1,7)
    canvas.delete('cislo')
    canvas.create_text(175,50,text=body,tag='cislo',font='Arial 50')
    canvas.create_text(100,150,text=cislo1,tag='cislo',font='Arial 25')
    canvas.create_text(250,150,text=cislo2,tag='cislo',font='Arial 25')
    print(cislo1)
    print(cislo2)
    canvas.after(250,hocico)
def rovnake():
    global cislo1,cislo2,body
    if cislo1==cislo2:
        body+=1
    else:
        body-=1
hocico()
button1 = tkinter.Button(text='Rovnaké', command=rovnake)
button1.pack()
