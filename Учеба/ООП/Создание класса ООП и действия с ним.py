print('Создание класса ООП и действия с ним')
print()
class TShip():
    x = 0
    v = 0
    def __init__(self,x,v):
        self.coordinate = x
        self.speed = v        
Ship = TShip(int(input('Введите координаты:')),
             int(input('Введите скорость:')))
print()
print('Координаты корабля:',Ship.coordinate)
print('Скорость корабля:',Ship.speed)

