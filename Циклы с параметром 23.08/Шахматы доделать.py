

M = int(input('Введите количество строк: '))
N = int(input('Ввведите количество знаков в строке: '))

for i in range(1,M+1):   
    for j in range(1,N+1):
        if i % 2 == 0:
            print(' ', end = '')
        print('*', end = ' ')   
    print()