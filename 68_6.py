import tkinter
canvas = tkinter.Canvas(height=400,width=400)
canvas.pack()
x=400
y=200
def kresli():
    global x,y
    slovo=entry1.get()
    if slovo!='':
        canvas.delete('all')
        canvas.create_text(x,y,text=slovo,font='Arial 20')
        x-=5
    if x<-100:
        x=400
    canvas.after(50,kresli)

entry1 = tkinter.Entry()
entry1.pack()
        
kresli()
