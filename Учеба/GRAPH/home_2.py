from graph import*

def frame():
    penColor('black')
    brushColor('green')
    rectangle(100,100,200,200)

    
def roof():
    penColor(255,255,255)
    brushColor('brown')
    polygon([(90,100),(150,50),(210,100),(90,100)])

    
def window():
    penColor(0,0,0)
    penSize(3)
    brushColor('black')
    rectangle(120,120,150,170)
    line(120,140,150,140)
    line(135,140,150,170)

def home():
    frame()
    roof()
    window()

home()

run()
