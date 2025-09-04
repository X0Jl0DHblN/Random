print('Результат сравнения чисел')

X = int(input('Введите первое число: '))
Y = int(input('Введите второе число: '))

def max_meaning (a,b):
    if a > b:
        return print('>')
    elif a == b:
        return print('<')
    else:
        return print('=')
          
max_meaning(X,Y)
