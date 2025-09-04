print('Возведение в стапень')

a = float(input('Введите число: '))
b = float(input('Введите степень: '))

def exponent(x,y):
    exp = x**y
    return exp
c = exponent(a,b)
print('{} в степени {} равняется {:2.2f}'.format(a,b,c))