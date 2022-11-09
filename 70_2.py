import tkinter
from random import *
canvas = tkinter.Canvas(height=400,width=400)
canvas.pack()
    
spravne=('byt','umyvacka','pizza')
nespravne=('bit','umivacka','pyzza')
slovo=''
yy=0
body=0
start=1
def trispinavemena():
    global hocico,slovo
    hocico=randrange(3)
    if hocico==1:
        slovo=choice(spravne)
    else:
        slovo=choice(nespravne)
def volaco():
    global hocico,slovo,yy,start
    if start==1:
        if yy==0:
            trispinavemena()
        canvas.delete('all')
        canvas.create_text(200,yy,text=slovo,font='Arial 20')
        yy+=10
        canvas.after(50,volaco)
        if yy>400:
            yy=0
def klik(suradnice):
    global yy,hocico,body,start
    x=suradnice.x
    y=suradnice.y
    if yy-20<y<yy+20 and hocico==1 and 220>x>180:
        body+=1
    if yy-20<y<yy+20 and hocico==0 and 220>x>180:
        body-=2
    if body>10:
        start=0
        canvas.delete('all')
        canvas.create_text(200,200,text='si zabil a vyhral si túto šialôčku ',font='Arial 20')
    print(body)
canvas.bind('<Button-1>',klik)
volaco()
