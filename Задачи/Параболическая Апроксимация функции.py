from math import *

print('Параболическая апроксимация')


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
    return det

n = int(input('Введите количество точек: '))

# =============================================================================
# X = [int(input('Введите значение X: ')) for i in range(n)]
# 
# Y = [int(input('Введите значение Y: ')) for i in range(n)]
# =============================================================================

X = [2, 6, 10, 14, 18]
Y = [9, 10, 12, 19, 20]


Sum_X = 0
Sum_Y = 0
Sum_X2 = 0
Sum_X3 = 0
Sum_X4 = 0
Sum_XY = 0
Sum_X2Y = 0
    
for i in range(n):
    Sum_X += X[i]
    Sum_Y += Y[i]
    Sum_X2 += X[i] * X[i]
    Sum_X3 += X[i] ** 3
    Sum_X4 += X[i] ** 4
    Sum_XY += X[i] * Y[i]
    Sum_X2Y += X[i] ** 2 * Y[i]

S1 = Sum_X
S5 = Sum_Y
S2 = Sum_X2
S3 = Sum_X3
S4 = Sum_X4
S6 = Sum_XY
S7 = Sum_X2Y



A = [[n,S1,S2],[S1,S2,S3],[S2,S3,S4]]
A1 = [[S5,S1,S2],[S6,S2,S3],[S7,S3,S4]]
A2 = [[n,S5,S2],[S1,S6,S3],[S2,S7,S4]]
A3 = [[n,S1,S5],[S1,S2,S6],[S2,S3,S7]]
N = 3


D = int(Det(A,N))
D1 = int(Det(A1,N))
D2 = int(Det(A2,N))
D3 = int(Det(A3,N))


a0 = D1 / D
a1 = D2 / D
a2 = D3 / D

print('Переменные полинома 2-го порядка a0 = {:.4f}, a1 = {:.4f}, a2 = {:.4f} '.format(a0,a1,a2))

x = float(input('Введите значение по оси x: '))

P_x = a0 + a1 * x + a2 * x ** 2
print('Тогда значение функции P(x) = {:.2f}'.format(P_x))


# =============================================================================
# Det(A1,N)
# Det(A2,N)
# Det(A3,N)
# =============================================================================




