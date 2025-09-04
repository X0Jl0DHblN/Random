
N = int(input('Введите количество точек: '))
print()
print('Значение Х', '  |  Значение У')
x = -4.5

for i in range(N):
    x += 0.5 
    if x >= 0:
        y = x
    else:
        y = -(x)
    print('{:7.2f}      |  {:7.2f}' .format(x,y))    