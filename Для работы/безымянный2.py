import numpy as np

arr = np.arange(45)
print(arr[12:43])


print('\n')


zero = np.zeros(12)
zero[4] = 1
print(zero)


print('\n')

matrix = np.arange(9).reshape(3,3)
print(matrix)

print('\n')

m1 = np.arange(15).reshape(5,3)
m2 = np.arange(6).reshape(3,2)
print(m1)
print('\n')
print(m2)
print('\n')
res = np.dot(m1,m2)
print(res)
print('\n')


arr = np.zeros((10, 10))
arr[1:-1, 1:-1] = 1
print(arr)

print('\n')

vek = np.random.rand(10)
print('Вектор: \n',vek)
print('\n')
vek.sort()
print('Отсортированный вектор: \n',vek)

print('\n')