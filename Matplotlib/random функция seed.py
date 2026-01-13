import numpy as np

np.random.seed(421)
print('Первые 5 случайных чисел в диапазоне [0,1): ')
print(np.random.rand(5))
print('\n следующие 5 случайных чисел: ')
np.random.seed(42)
print(np.random.rand(5))