import numpy as np

A = np.array([[3,-1,2],[1,4,-1],[2,3,1]])
B = np.array([[-4],[10],[8]])
print(A)
print('\n')
print(B)
print('\n')


detA = np.linalg.det(A)
print(detA)
print('\n')

Ax = np.matrix(A)
Ax[:,0] = B
print(Ax)
detAx = np.linalg.det(Ax)
print('\n')
Ay = np.matrix(A)
Ay[:,1] = B
print(Ay)
detAy = np.linalg.det(Ay)
print('\n')
Az = np.matrix(A)
Az[:,2] = B
print(Az)
detAz = np.linalg.det(Az)

print('\n')
x = detAx/detA
y = detAy/detA
z = detAz/detA
print(x,y,z)
