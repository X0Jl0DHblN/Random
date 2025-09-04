print('Рекурсивная функция вычисления факториала')

def F(n):
    if n == 0:
        return 1
    else:
        return F(n-1)*n

N = int(input('Ввведите значение: '))

Res = F(N)

print('Факториал числа {} равен {}'.format(N,Res))

