print('Поиск НОК')

m = int(input('Введите первое число: '))
n = int(input('Введите второе число: '))

def NOD(m,n):
    if m == n:
        return m
    if m < n:
        return NOD(m, n - m)
    else:
        return NOD(m - n, n)

c = NOD(m,n)

NOK = m * n / c

print('Наименьшее общее кратное для чисел {} и {} равняется {}'.format(m,n,int(NOK)))