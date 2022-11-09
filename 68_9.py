import tkinter
canvas = tkinter.Canvas(height=355)
canvas.pack()

y=0
r=0
canvas.create_oval(50,325,250,350)
canvas.create_oval(50,275,250,300)
canvas.create_line(50,290,50,340)
canvas.create_line(250,290,250,340)
start=1
def hocico():
    global y,start,r
    if start==1:
        canvas.delete('kvapka')
        canvas.create_oval(140,y,165,y+25,fill='blue',tag='kvapka')
        if r>0:
            canvas.create_oval(150-r,325,150+r,350,tag='kvapka',fill='blue',outline='')
        y+=10
        canvas.after(50,hocico)
        canvas.create_text(250,50,text=r//10,font='Arial 20',tag='kvapka')
        if y>320:
            y=0
            r+=10
        if r>100:
            r=100
def startuj():
    global start
    if start==1:
        start=0
    else:
        start=1
        hocico()
print(start)
button1 = tkinter.Button(text='start/stop', command=startuj)
button1.pack()
hocico()
