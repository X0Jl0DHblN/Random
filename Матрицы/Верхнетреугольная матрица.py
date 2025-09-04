from random import*
print()
print('Верхнетреугольная матрица')

M = int(input('Введите размерность матрицы: '))
print()
A = [[0] * M for i in range(M)]
for i in range(M):
    for j in range(M):
        A[i][j] = randint(1,10)
for i in range(M):
    for j in range(M):
        print('{:4d}'.format(A[i][j]), end = '')
    print() 

print()
print('Преобразование матрицы в верхнетреугольную')
print()
for i in range(M):
    for j in range(M):
        if i > j:                               # нижнетреугольная наоборот 
            A[i][j] = 0
        print('{:4d}'.format(A[i][j]), end = '')
    print()    
    
