


class TPen():
    def __init__(self):
        self.__color = '000000'
    def getColor(self):
        return self.__color
    def setColor(self,newColor):
        if len(newColor) == 6:
            self.__color = newColor
        else:
            self.__color = '000000'
            
Pen =TPen()
Pen.setColor('FF0000')
print('Цвет пера: ', Pen.getColor())