from Graph import*
           
class TShip():
    SHIP_Y = 200
    def __init__(self,x0,v0,fileName):
        self.x = x0 if x >= 0 else 0
        self.v = v0
        self.image = image(self.x, TShip.SHIP_Y,fileName)
    def move(self):
        moveObjectBy(self.image,self.v,0)
fps = 20
updatePeriod = round(1000/fps)

Ship = TShip(5,0,3,‪'P:\shipFolder\Ship.jpg')

def updare():
    Ship.move

onTimer(update,updatePeriod)

run()
