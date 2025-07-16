from graph import*
from os import*

brushColor('blue')
rectangle(0,0,400,400)
R = 10
x0 = 10
y0 = 200
penColor('yellow')
brushColor('yellow')
obj = circle(x0,y0,R)
dx = 5
dy = 0


def update():
    global x0
    moveObjectBy(obj,dx,dy)
    x0 = x0+dx
    if x0 >= 400 - R:
        close()

text = 'ЖИЗНЬ В ДВИЖЕНИИ'

label(text,130,100)


def pressKey(event):
    if event.keycode == VK_ESCAPE:
        system('pause')
        
onTimer(update,200)  
onKey(pressKey)

run()
