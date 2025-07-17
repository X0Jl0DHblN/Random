from graph import*
canvasSize(1000,1000)
def frame(x,y):
    penColor('black')
    brushColor('green')
    rectangle(x+100,y+100,x+200,y+200)

    
def roof(x,y):
    penColor(255,255,255)
    brushColor('brown')
    polygon([(x+90,y+100),(x+150,y+50),(x+210,y+100),(x+90,y+100)])

    
def window(x,y):
    penColor(0,0,0)
    penSize(3)
    brushColor('black')
    rectangle(x+120,y+120,x+150,y+170)
    line(x+120,y+140,x+150,y+140)
    line(x+135,y+140,x+150,y+170)

def home(x,y):
    frame(x,y)
    roof(x,y)
    window(x,y)

home(10,10)
home(150,150)

run()
