print('Метод Ньютона(метод касательных)')



a = int(input('Введите левое значение: '))
b = int(input('Введите правое значение: '))
eps = float(input('Введите приблежение: '))

def f(x):
    return x ** 2 + 3 * x - 4

def F(x):
    return 2 * x + 3

x0 = b
while abs(f(x0)) > eps:
    x1 = x0 - f(x0) / F(x0)
    x0 = x1
print('Приближенное значение корня равняется: {:.2f}'.format(x0))    
    
    
    
    
    
    