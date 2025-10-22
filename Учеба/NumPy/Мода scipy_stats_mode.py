import numpy as np
from scipy import stats
print('\n')
data = np.array([1,2,2,3,3,3,4,4,4,5,6,7,7,8,8,8,8,9])
print('Массив:',data)
print('\n')
Moda = stats.mode(data)
print('Moda массива= ', Moda.mode)
print('Количество повторений = ',Moda.count)
print('\n')
values,counts = np.unique(data,return_counts=True)
print('Все уникальные значения массива: ',values)
print('Количество повторений значений в исходном массиве: ',counts)
print('\n')
ModaV = values[np.argmax(counts)]
print('Мода массива:',ModaV)
print('\n')