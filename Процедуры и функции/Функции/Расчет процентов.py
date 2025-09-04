print('Расчет процентов')

X = int(input('Введите число: '))
Y = int(input('Введите количество процентов от числа: '))
 
def Procent(a,b):
    Proc = a/100*b
    return Proc

res = Procent(X,Y) 

print('{} процентов от {}, составляет {}'.format(Y, X, res))




