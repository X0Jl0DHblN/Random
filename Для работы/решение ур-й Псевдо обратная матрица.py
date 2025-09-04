import numpy as np

A = np.array([[2,3]])
B = np.array([[1]])
print(A)
print('\n')
print(B)
X = np.linalg.pinv(A)@B
print('Решение:',X)