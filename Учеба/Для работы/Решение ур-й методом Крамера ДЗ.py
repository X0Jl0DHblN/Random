import numpy as np

A = np.array([[1,2,1,0],[0,1,3,1],[4,0,1,1],[1,1,0,5]])
B = np.array([[8],[15],[11],[23]])
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
Au = np.matrix(A)
Au[:,3] = B
print(Au)
detAu = np.linalg.det(Au)

print('\n')
x = detAx/detA
y = detAy/detA
z = detAz/detA
u = detAu/detA
print(x,y,z,u)
