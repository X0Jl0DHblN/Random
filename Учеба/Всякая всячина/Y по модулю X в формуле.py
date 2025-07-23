
N = int(input('Введите количество точек: '))
print()
print('Значение Х', '  |  Значение У')
x = -4.5
y = x
for i in range(N):
    x += 0.5 
    if x >= 0:
        y = (x - 2) + (x + 1)
    else:
        y = -(x - 2) + (-(x + 1))
    print('{:7.2f}      |  {:7.2f}' .format(x,y)) 