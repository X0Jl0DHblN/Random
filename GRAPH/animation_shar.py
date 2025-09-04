from graph import*
brushColor('blue')
rectangle(0,0,450,450)

x0 = 20
y0 = 200
penColor('yellow')
brushColor('yellow')
obj = circle(x0,y0,10)

def update():
    moveObjectBy(obj,1,0)

onTimer(update,20) 
run()
