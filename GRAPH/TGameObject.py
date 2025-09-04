from graph import*
from random import*

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 400
fps = 20
updatePeriod = round(1000/fps)

class TGameObject:
    def __init__(self,x,y,width,height):
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        if not hasattr(self, 'update'):
            raise NotImplementedError ('Нельзя создать такое объект')
        @property
        def x(self):
            return self._x
        def y(self):
            return self._y
        def width(self):
            return self._width
        def height(self):
            return self._height

class TBlackHole(TGameObject):
    def __init__(self,xCenter,yCenter,radius):
        TGameObject.__init__(self,xCenter,yCenter,2*radius,2*radius)
        brushColor('black')
        self._image = circle(xCenter,yCenter,radius)
    def update(self):
        pass

class TPulsar(TBlackHole):
    def __init__(self,xCenter,yCenter,radius):
        TBlackHole.__init__(self,xCenter,yCenter,radius)
        changeFillColor(self._image,'brown')
    def update(self):
        self.__changeRadius(randint(5,20))
    def __changeRadius(self,newRadius):
        self.__width = 2*newRadius
        self.__height = 2*newRadius
        changeCoords(self._image,
                     [(self._x-newRadius, self._y-newRadius),
                      (self._x+newRadius, self._y+newRadius)])
    

windowSize(SCREEN_WIDTH, SCREEN_HEIGHT)
canvasSize(SCREEN_WIDTH, SCREEN_HEIGHT)

NUMBER_OF_BLACKHOLES = 10
blackHoles = []

NUMBER_OF_PULSAR = 10
pulsars = []

for i in range (NUMBER_OF_BLACKHOLES):
    blackHoles.append(TBlackHole(randint(0,SCREEN_WIDTH),randint(0,SCREEN_HEIGHT),randint(10,20)))
for i in range (NUMBER_OF_PULSAR):
    pulsars.append(TPulsar(randint(0,SCREEN_WIDTH),randint(0,SCREEN_HEIGHT),randint(10,20)))
def update():
    for bh in blackHoles:
        bh.update()
    for ps in pulsars:
        ps.update()
        
    
        
onTimer(update,updatePeriod)

run()
        
        
