

print('Функция определения наибольшего из введенных чисел')

X = int(input('Введите первое число: '))
Y = int(input('Введите второе число: '))

def max_meaning (a,b):
    if a > b:
        return print('Наибольшее из введенных чисел:',a)
    elif a < b:
        return print('Наибольшее из введенных чисел:',b) 
    else:
        return print('Ввведенные числа равны')
          
max_meaning(X,Y)
