from graph import*

x=int(input('Введите точку на оси ординат: '))
y=int(input('Введите точку на оси ординат: '))
N = 20
h = round(((x+100) - x)/ N)


penColor('red')
penSize(3)
rectangle(x,y,x+100,y+40)

for x in range(x,x+100,h):
    penColor('gray')
    penSize(1)
    line(x+h,y+1,x+h,y+39)
    
run()
