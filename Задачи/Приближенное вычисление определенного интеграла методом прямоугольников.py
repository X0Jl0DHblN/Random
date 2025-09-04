print('Приближенное вычисление определенного интеграла методом прямоугольников')

a = float(input('Введите левое значение: '))
b = float(input('Введите правое значение: '))
n = int(input('Введите количество частей: '))

def f(x):
    return x ** 2 + 1

h = (b - a) / n

Sum_f = 0

for i in range(n):
    x = a + h * i
    Sum_f += f(x)
O_intgr = h * Sum_f    
print('Определенный интеграл равняестся: {:.2f}'.format(O_intgr))   