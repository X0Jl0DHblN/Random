print('Мутация матрицы')


M = int(input('Введите количество строк: '))
N = int(input('Введите количество столбцов: '))
 
A = [[0] * N for i in range(M)]
B = [[0] * (N + 1) for i in range(M + 1)]

for j in range(N):
    Sum_post = 0
    for i in range(M):
        A[i][j] = int(input('Введите элемент: '))
        Sum_post += A[i][j]
        B[i][j] = A[i][j]
    B[M][j] = Sum_post
        
for i in range(M):
    Sum_row = 0
    for j in range(N):
        Sum_row += A[i][j]
    B[i][N] = Sum_row         
    
print()
for i in range(M):
    for j in range(N):
        print('{:4d}'.format(A[i][j]), end = '')
    print()   
    
print()    
 
for i in range(M + 1):
    for j in range(N + 1):
        print('{:4d}'.format(B[i][j]), end = '')
    print()  
    
print()    