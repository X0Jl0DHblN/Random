from random import*

print('Создание матрицы с рандомным заполнением и классическим выводом')

M = int(input('Введите количество строк: '))
N = int(input('Введите количество столбцов: '))

A = [[0] * N for i in range(M)]

for i in range(M):
    for j in range(N):
        A[i][j] = randint(1,10)
        
print(A)  
print()
for i in range(M):
    for j in range(N):
        print('{:4d}'.format(A[i][j]), end = '')
    print()
   
