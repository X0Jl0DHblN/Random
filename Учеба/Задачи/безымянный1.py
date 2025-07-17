from math import *

print('Нахождение определителя матрицы методом Гауса')

N = int(input('Введите размерность матрицы: '))

A = [[0] * N for i in range(N)]

print('Введите матрицу системы уравнений')

for i in range(N):
    for j in range(N):
        A[i][j] = float(input()) 

print(A)


det = 1
for k in range(N):
    Max = abs(A[k][k])
    R = k
    for i in range(k+1,N-1):
        if abs(A[i][k]) > Max:
            Max = abs(A[i][k])
            R = i
    if R != k:
        det *= -1
    for j in range(N):
        temp = A[k][j]
        A[k][j] = A[R][j]
        A[R][j] = temp
for i in range(k+1,N-1):
    M = A[i][k] / A[k][k]
    for j in range(k,N-1):
        A[i][j] = A[i][j] - M * A[k][j]      
for i in range(N):
    det = det * A[i][j]
print(det)  