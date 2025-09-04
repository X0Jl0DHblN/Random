from graph import*
x = 0
y = 0

def rhomb(x,y):
    penColor('red')
    penSize(2)
    polygon([(x+20,y+70),(x+40,y+50),(x+60,y+70),(x+40,y+90)])
def figure(x,y):
    for x in range(0,120,40):
        rhomb(x,40)
    for y in range(0,120,40):
        rhomb(40,y) 

for x in range(0,500,120):
    figure(x,y)



run()
