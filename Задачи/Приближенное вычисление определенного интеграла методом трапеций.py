print('Приближенное вычисление определенного интеграла методом трапеций')

a = float(input('Введите левое значение: '))
b = float(input('Введите правое значение: '))
n = int(input('Введите количество частей: '))

def f(x):
    return x ** 2 + 1

h = (b - a) / n

Sum_f = 0


for i in range(1,n + 1):
    x = a + h * i
    Sum_f += f(x)
Sum = (f(a) + f(b)) / 2 + Sum_f
O_intgr = h * Sum    
print('Определенный интеграл равняестся: {:.2f}'.format(O_intgr))