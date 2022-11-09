import tkinter,random
canvas = tkinter.Canvas(height=600)
canvas.pack()
cislo=60
start=1
spravny=random.randrange(1,5)
def odpocet():
    global cislo,start
    canvas.delete('all')
    canvas.create_text(175,100,text=str(cislo),font='Arial 50',fill='red')
    cislo-=1
    if start==1:
        canvas.after(1000,odpocet)
    if cislo==0:
        start=0
def modry():
    global start
    tip=1
    if tip==spravny:
        canvas.delete('all')
        canvas.create_text(175,100,text='Nemvybuchol si',font='Arial 50',fill='red')
    else:
        canvas.create_text(175,100,text='Vybuchol si',font='Arial 50',fill='red')
    start=0
def cerveny():
    global start
    tip=2
    if tip==spravny:
        canvas.delete('all')
        canvas.create_text(175,100,text='Nemvybuchol si',font='Arial 50',fill='red')
    else:
        canvas.create_text(175,100,text='Vybuchol si',font='Arial 50',fill='red')
    start=0
def zlty():
    global start
    tip=3
    if tip==spravny:
        canvas.delete('all')
        canvas.create_text(175,100,text='Nemvybuchol si',font='Arial 50',fill='red')
    else:
        canvas.create_text(175,100,text='Vybuchol si',font='Arial 50',fill='red')
    start=0
def zeleny():
    global start
    tip=4
    if tip==spravny:
        canvas.delete('all')
        canvas.create_text(175,100,text='Nemvybuchol si',font='Arial 50',fill='red')
    else:
        canvas.create_text(175,100,text='Vybuchol si',font='Arial 50',fill='red')
    start=0
    

print(spravny)
if start==1:
    odpocet()
button1 = tkinter.Button(text='Modrý', command=modry)
button1.pack()
button2 = tkinter.Button(text='Červený', command=cerveny)
button2.pack()
button3 = tkinter.Button(text='Žltý', command=zlty)
button3.pack()
button4 = tkinter.Button(text='Zelený', command=zeleny)
button4.pack()
