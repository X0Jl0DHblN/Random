
print('Свойства в классе')

class TPen():
    def __init__(self):
        self.__color = '000000'
    def __getColor(self):
        return self.__color
    def __setColor(self, newColor):
        if len(newColor) == 6:
            self.__color = newColor
        else:
            self.__color = '000000'
            
    color = property(__getColor, __setColor)

pen = TPen()    
pen.color = 'FF0000'
print('Цвет пера: ', pen.color)
            

