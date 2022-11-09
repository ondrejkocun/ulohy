import tkinter
canvas = tkinter.Canvas(height=600)
canvas.pack()



def balon(x,y):
    canvas.create_oval(x,y,x+30,y+30)
    canvas.create_line(x,y+15,x+15,y+50)
    canvas.create_line(x+30,y+15,x+15,y+50)
    canvas.create_rectangle(x+5,y+50,x+25,y+55)
def lod(x,y):
    canvas.create_line(x,y,x+80,y,x+60,y+30,x+20,y+30,x,y)
    canvas.create_line(x+40,y,x+40,y-60,x+60,y-30,x+40,y-20)
def kresli(suradnice):
    x=suradnice.x
    y=suradnice.y
    if y>400:
        lod(x,y)
    else:
        balon(x,y)
canvas.create_rectangle(0,400,400,600,fill='blue')
canvas.bind('<Button-1>',kresli)
