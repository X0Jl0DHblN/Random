import numpy as np


A = np.array([[1,0,2,0,0],[0,1,0,2,0],[2,0,4,0,0]])
print(A)
print()
r = np.linalg.matrix_rank(A)
print('Ранг матрицы А равен:',r)

