import tkinter,random
canvas = tkinter.Canvas()
canvas.pack()
hocico=10
def kresli():
    global hocico
    text1=entry1.get()
    x=random.randrange(400)
    y=random.randrange(300)
    canvas.create_text(x,y,text=text1,angle=hocico)
    canvas.after(250,kresli)
    hocico+=10
    if hocico>90:
        hocico=10
def vymaz(event):
    canvas.delete('all')
canvas.bind('<Button-1>',vymaz)
entry1 = tkinter.Entry()
entry1.pack()
kresli()
