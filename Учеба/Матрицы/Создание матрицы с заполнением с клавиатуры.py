print('Создание матрицы с заполнением с клавиатуры')

M = int(input('Введите количество строк: '))
N = int(input('Введите количество столбцов: '))

A = [[0] * N for i in range(M)]

for i in range(M):
    for j in range(N):
        A[i][j] = int(input('Введите элемент: '))
print(A)    