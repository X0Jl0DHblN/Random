from math import *

print('Нахождение определителя матрицы методом Гауса')


def Det(A,N):
    det = 1
    for k in range(N):
        Max = abs(A[k][k])
        R = k
        for i in range(k+1,N):
            if abs(A[i][k]) > Max:
                Max = abs(A[i][k])
                R = i
        if R != k:
            det = -det
        for j in range(N):
            temp = A[k][j]
            A[k][j] = A[R][j]
            A[R][j] = temp
        for i in range(k+1,N):
            M = A[i][k] / A[k][k]
            for j in range(k,N):
                A[i][j] = A[i][j] - M * A[k][j]      
    for i in range(N):
        det = det * A[i][i]
    print(det) 

N = int(input('Введите размерность матрицы: '))

A = [[0] * N for i in range(N)]

print('Введите матрицу системы уравнений')

for i in range(N):
    for j in range(N):
        A[i][j] = int(input()) 
print(A)

Det(A,N)     