import numpy as np

A = np.array([[1,5,-2,-3],[7,2,-3,-4],[1,1,1,1],[2,3,2,-3],[1,-1,-1,-1]])
B = np.array([[1],[2],[5],[4],[-2]])
print(A)
print('\n')
print(B)
print('\n')

X = np.linalg.pinv(A)@B
print('\n')
print(X)