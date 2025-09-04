from Graph import*
           
class TShip():
    SHIP_Y = 200
    def __init__(self,x0,v0,fileName):
        self.x = x0 if x >= 0 else 0
        self.v = v0
        self.image = image(self.x, TShipSHIP_Y,fileName)
    def move(self):
        moveObjectBy(self.image,self.v,0)

Ship = TShip(5,0,‪C:\ShipImage\Ship.png)
            


