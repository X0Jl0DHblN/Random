print('Рекурсивная функция вычисления степени числа')

def F(x,n):
    if n == 0:
        return 1
    else:
        return F(x,n - 1) * x

X = int(input('Введите число: '))
N = int(input('Введите степень числа: '))
 

Res = F(X,N)

print('Число {} в степени {} равно {}'.format(X,N,Res))