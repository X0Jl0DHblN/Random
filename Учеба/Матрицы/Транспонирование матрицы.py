print('Транспонирование матрицы')


from random import*

M = int(input('Введите количество строк: '))
N = int(input('Введите количество столбцов: '))

A = [[0] * N for i in range(M)]
B = [[0] * M for i in range(N)]

for i in range(M):
    for j in range(N):
        A[i][j] = randint(1,10)
           
print()
for i in range(M):
    for j in range(N):
        B[j][i] = A[i][j]
        print('{:4d}'.format(A[i][j]), end = '')
    print()
print()
print('Транспонирование матрицы')
print()
for i in range(N):
    for j in range(M):
        print('{:4d}'.format(B[i][j]), end = '')
    print()