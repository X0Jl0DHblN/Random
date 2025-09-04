print('Алгоритм Герона Александрийского')

from math import*

A = int(input('Введите число: '))
x = int(input('Введите число: '))
eps = float(input('Введите приблежение: '))

sqrt = sqrt(A)
print(sqrt)

x1 = (1 / 2) * (x + A / x)

while abs(x1 ** 2 - A) >= eps:   
    print(x1)
