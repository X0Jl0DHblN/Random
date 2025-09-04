import numpy as np

A = np.array([[1,-1,1,-1],[1,2,-2,-1],[2,-1,-3,2],[1,2,3,-6]])
B = np.array([[-2],[-5],[-1],[-10]])
print(A)
print('\n')
print(B)
print('\n')

det = np.linalg.det(A)  
print(det) # равно 0

X = np.linalg.solve(A,B)
print(X)


 

