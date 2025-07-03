import numpy as np


X = np.array([[3,-1,2],[1,4,-1],[2,3,1]])
print(X)
print()
Y = np.matrix([[-4],[10],[8]])
print(Y)
print()
# =============================================================================
# X =  np.matrix(['x','z','y'])
# print(X)
# =============================================================================
A_inv = np.linalg.inv(X)
print(A_inv)

X = A_inv.dot(Y)
print(X)
print('\n')
C = 14 * A_inv
print(C)