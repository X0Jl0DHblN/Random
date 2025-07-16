print('Решение системы уравнений методом Гауса')

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

print('Расширинная матрица')

for i in range(N):
    for j in range(N):
        print('{:7.2f}'.format(A[i][j]), end = '')
    print(' |','{:2.2f}'.format(B[i]), end = '')   
    print()
