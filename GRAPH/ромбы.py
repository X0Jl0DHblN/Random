from graph import*
x = 0
y = 0

def rhomb(x,y):
    penColor('red')
    penSize(2)
    polygon([(x+20,y+30),(x+30,y+10),(x+40,y+30),(x+30,y+50),(x+20,y+30)])


x = int(input('Введите точку на оси ординат: '))
y = int(input('Введите точку на оси абсцисс: '))

for x in range(0,61,10):
    for y in range(0,61,10):
        rhomb(x,y)
    

run()
