print('Результат сравнения чисел')

X = int(input('Введите первое число: '))
Y = int(input('Введите второе число: '))

def max_meaning (a,b):
    if a > b:
        return '>'
    elif a < b:
        return '<'
    else:
        return '='
          
res = max_meaning(X,Y)
print(X,res,Y)