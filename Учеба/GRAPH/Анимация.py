from graph import*
brushColor('blue')
rectangle(0,0,400,400)
x = 100
y = 100
penColor('yellow')
brushColor('yellow')
obj = circle(x,y,10)
def update():
    moveObjectBy(obj,5,0)
    if xCoord(obj) >=380:
        close()
penColor('yellow')
penSize(3)
text = 'ЖИЗНЬ В ДВИЖЕНИИ'
label(text, 130,50)
onTimer(update,50)        
run()
