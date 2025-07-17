print('Метод деления пополам, Дихотомия')

a = float(input('Введите первое число: '))
b = float(input('Введите второе число: '))
eps = float(input('Введите приблежение: '))

def F1(x):
    return x ** x

def F2(x):
    return 1 / x

def solve(a, b, eps):
    while abs(b - a) > eps:
        c = (a + b) / 2
        fa = F1(a) - F2(a)
        fb = F1(b) - F2(b)
        if fa * fb < 0:
            b = c
        else:
            a = c
    return (a + b) / 2

root = solve(a, b, eps)
print('Приближенное значение корня уравнения равняется {}'.format(root))            
