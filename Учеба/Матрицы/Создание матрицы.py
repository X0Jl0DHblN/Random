print('Создание матрицы')

M = int(input('Введите количество строк: '))
N = int(input('Введите количество столбцов: '))

A = []

for i in range(M):
    A.append([0] * N)
#print(A)

A[0][0] = 1

print(A)   