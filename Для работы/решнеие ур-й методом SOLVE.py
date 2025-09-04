import numpy as np

A = np.array([[3,-1,2],[1,4,-1],[2,3,1]])
B = np.array([[-4],[10],[8]])
print(A)
print('\n')
print(B)
print('\n')

X = np.linalg.solve(A,B)
print(X)