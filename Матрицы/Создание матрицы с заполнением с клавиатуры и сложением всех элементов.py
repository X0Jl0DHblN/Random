print('Создание матрицы с заполнением с клавиатуры и сложением всех элементов')

M = int(input('Введите количество строк: '))
N = int(input('Введите количество столбцов: '))

A = [[0] * N for i in range(M)]

for i in range(M):
    for j in range(N):
        A[i][j] = int(input('Введите элемент: '))  
Sum = 0
print()
for i in range(M):
    for j in range(N):
        Sum += A[i][j]
        print('{:2d}'.format(A[i][j]), end = '')
    print()
   
print(Sum) 