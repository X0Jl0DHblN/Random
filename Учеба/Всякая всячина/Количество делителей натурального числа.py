print('Количество делителей натурального числа')

N = int(input('Введите число: '))

def Div(n):
    d = 2
    count = 0

    while d <= N:
        if N % d == 0:
            count += 1
        d += 1
    return count + 1    
        
print('Количество делителей натурального числа {}, равняется {}'.format(N, Div(N)))
        