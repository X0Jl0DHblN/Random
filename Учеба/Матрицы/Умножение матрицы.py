print('Умножение матрицы')
 
from random import*
 
M = int(input('Введите размер 1: '))
K = int(input('Введите размер 2: '))
N = M
 
A = [[0] * K for i in range(M)]
B = [[0] * N for i in range(K)]
C = [[0] * N for i in range(M)]

for i in range(M):
    for j in range(K):
        A[i][j] = randint(1,10)  
for i in range(K):
    for j in range(N):
        B[i][j] = randint(1,10)
for i in range(M):
    for j in range(N):
        Sum = 0
        for l in range(K):
            Sum += A[i][l] * B[l][j]
        C[i][j] = Sum
    print()

for i in range(M):
    for j in range(K):
        print('{:4d}'.format(A[i][j]), end = '')
    print() 
print()
for i in range(K):
    for j in range(N):
        print('{:4d}'.format(B[i][j]), end = '')
    print() 
print()    
for i in range(M):
    for j in range(N):
        print('{:4d}'.format(C[i][j]), end = '')
    print()   