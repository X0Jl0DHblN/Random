from math import*

print('Функция расчета объёма цилиндра')

R = float(input('Введите радиус основания (см): '))
H = float(input('Введите высоту цилиндра (см): '))

def volume (a,b):
    V = pi * a**2 * b
    return print('Объём цилиндра {:0.5} сантиметров в кубе'.format(V))
volume(R,H)
#print('Объём цилиндра {:0.5} сантиметров в кубе'.format(Vol))