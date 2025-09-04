import numpy as np

m = np.matrix('1 2 3 4; 5 6 7 8; 9 1 5 7')
print(m)
print()
print(type(m)) #<class 'numpy.matrix'>
print()
print(m.shape)
print()
m = np.array(m)
print(type(m)) #<class 'numpy.ndarray'>
print()
maximum = m.max()
print('Максимальное значение в матрице: ',maximum)
print()
maximum_1 = np.max(m)
print('Максимальное значение в матрице: ',maximum_1)
print()
print(m.max(axis = 1))
print(m.median())