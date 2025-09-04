print('Расчет процентов')

X = int(input('Введите число: '))
Y = int(input('Введите количество процентов от числа: '))
 
def Procent(a,b):
    Proc = a/100*b
    return print('{} процентов от {}, составляет {}'.format(Y, X, Proc))
 
Procent(X,Y) 




