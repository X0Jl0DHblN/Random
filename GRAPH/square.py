from graph import*
def square(x,y,a,b):
    rectangle(x,y,x+a,y+a)
    rectangle(b,y,b+(2*a),y+(2*a))




a = int(input('Введите длину стороны: '))
x = int(input('Введите точку по оси X: '))
y = int(input('Введите точку по оси Y: '))
b = x+(a*2)

square(x,y,a,b)

run()
