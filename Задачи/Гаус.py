import numpy as np

N = int(input('Введите размерность системы уравнений: '))

A = [[0] * N for i in range(N)]

print('Введите матрицу системы уравнений')

for i in range(N):
    for j in range(N):
        A[i][j] = float(input()) 
   
B = [[0] * N for i in range(N)]

print('Введите матрицу свободных членов уравнения')

for i in range(N):
    B[i] = float(input())

# Прямой ход метода Гаусса
n = len(B)
for i in range(n):
    # Поиск максимального элемента в столбце i
    maxEl = abs(A[i][i])
    maxRow = i
    for k in range(i + 1, n):
        if abs(A[k][i]) > maxEl:
            maxEl = abs(A[k][i])
            maxRow = k
    # Обмен строками
    for k in range(i, n):
        tmp = A[maxRow][k]
        A[maxRow][k] = A[i][k]
        A[i][k] = tmp
    tmp = B[maxRow]
    B[maxRow] = B[i]
    B[i] = tmp
    # Приведение к верхнетреугольному виду
    for k in range(i + 1, n):
        c = -A[k][i] / A[i][i]
        for j in range(i, n):
            if i == j:
                A[k][j] = 0
            else:
                A[k][j] += c * A[i][j]
        B[k] += c * B[i]

# Обратный ход метода Гаусса
x = np.zeros(n)
for i in range(n - 1, -1, -1):
    x[i] = B[i]
    for j in range(i + 1, n):
        x[i] -= A[i][j] * x[j]
    x[i] /= A[i][i]

# Вывод результата
print("Result:")
print(x)