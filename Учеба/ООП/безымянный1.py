print('Создание класса ООП и действия с ним, кораблик')
print()
print('Типы кораблей:')
A = str('авианосец')
K = str('крейсер')
E = str('эсминц')
F = str('фрегат')
K = str('корвет')
D = str('десантные корабли')


           
class TShip():
    x = 0
    v = 0
    z = ' '
    def __init__(self,x,v,z):
        self.coordinate = x
        self.speed = v
        self.type = z
Ship = TShip(int(input('Введите координаты:')),
             int(input('Введите скорость:')),
             input('Введите тип корабля:'))

            


print('Корабль:',Ship.type)             
print('Координаты корабля:',Ship.coordinate)
print('Скорость корабля:',Ship.speed)