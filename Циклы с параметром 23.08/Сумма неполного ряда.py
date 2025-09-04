from math import*

print('Сумма неполного ряда')

N = int(input('Введите количество значений в ряду: '))

Sum = 0
sign = 1

for i in range(1, N + 1):
    Sum += (1 / (i*2 - 1)) * sign
    sign = - sign
print(Sum)
print(pi / 4)    