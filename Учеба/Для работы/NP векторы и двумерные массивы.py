import numpy as np


a = np.array([1,2,3])
b = np.array([[1],[2],[3]])
print()
print('Вектор:\n', a)
print('Размерность вектора: ', a.shape)
print()
print('Двумерный массив:\n', b)
print('Размерность двумерного массива: ', b.shape)
print('===========================================')
print()


a = a.T
b = b.T

print('Вектор а не изменился:\n', a)
print('Размерность вектора "а" не изменилась: ', a.shape)
print()
print('Транспонирование вектора "b":\n', b)
print('Размерность изменилась: ' , b.shape)

print('===========================================')
print()

A = np.array([1,2,3], dtype = 'int64')
print(A)
print(A.dtype)
print()
B = np.array([1,2,3], dtype = 'float')
print(B)
print(B.dtype)