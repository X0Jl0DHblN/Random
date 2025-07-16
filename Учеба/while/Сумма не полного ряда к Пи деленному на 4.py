from math import*

print('Вычисление Пи с заданной точностью')
print()
E = float(input('Задайте точность определения Пи: '))
Sum = 0
sign = 1
i = 1
while 1 / (2*i -1) > E:
    Sum = Sum + 1 / ((2*i - 1) * sign)
    i += 1
    sign = -sign
print('Сумма не полного ряда равна:', Sum)    
print('Значение Пи/4:', pi / 4)