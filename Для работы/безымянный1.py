import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[0,-1],[2,1]])
z = x * y
print(z)

w = np.dot(x,y)
print(w)

u = x.dot(y)
print(u)

arr = np.array([1,2])
arr1 = x.dot(arr)
print(arr1)