from graph import*
canvasSize(1000,1000)
def face(x,y,z):
    penColor('black')
    brushColor('green')
    rectangle((x+20),(y+160),(x+40)*z,(y+180)*z)

def roof(x,y):
    penColor('black')
    brushColor('green')
    polygon([(x+20,y+160),(x+30,y+150),(x+50,y+150),(x+40,y+160)])

def wall(x,y):
    penColor('black')
    brushColor('green')
    polygon([(x+40,y+160),(x+50,y+150),(x+50,y+170),(x+40,y+180)])


def cube(x,y,z):
    face(x,y,z)
    roof(x,y)
    wall(x,y)



x = int(input('Введите значение X:'))
y = int(input('Введите значение Y:'))
z = int(input('Введите значение Z:'))
cube(x,y,z)
run()





    
