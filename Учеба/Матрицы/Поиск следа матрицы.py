from random import*

print('Поиск следа матрицы')

M = int(input('Введите размерность матрицы: '))


A = [[0] * M for i in range(M)]

for i in range(M):
    for j in range(M):
        A[i][j] = randint(1,10)
        
print(A)  

print()
for i in range(M):
    for j in range(M):
        print('{:4d}'.format(A[i][j]), end = '')
    print()

sled = 0
Sum = 0
for i in range(M):
    sled += A[i][i]
    Sum += A[i][M-1-i]
    
print('След матрицы равняется: ', sled)
print('Сумма элементов матрицы по дополнительной диагонали равна: ', Sum)

