import tkinter,random
canvas = tkinter.Canvas(width=500)
canvas.pack()
start=1
x=20
x1=20
def carodejnica():
    global x,x1,start
    if start==1:
        posun=random.randrange(10)
        canvas.delete('all')

        for i in range(10):
            canvas.create_line(x,i*10,x+20,50)
        canvas.create_line(x+20,50,x+70,50)
        canvas.create_rectangle(x+40,60,x+60,30)
        canvas.create_oval(x+40,30,x+60,15)
        for i in range(10):
            canvas.create_line(x,i*10+100,x+20,150)
        canvas.create_line(x+20,150,x+70,150)
        canvas.create_rectangle(x+40,160,x+60,130)
        canvas.create_oval(x+40,130,x+60,115)
        x+=posun
        posun1=random.randrange(10)
        x1+=posun1
        canvas.after(50,carodejnica)
        if x>500:
            start=0
            canvas.create_text(100,150,text='Vyhrala prvá čarodejnica')
        if x1>500:
            start=0
            canvas.create_text(100,150,text='Vyhrala druhá čarodejnica')
carodejnica()
