import numpy as np

print('\n')
arr = np.array([4,8,6,5,3,2,8,9,2,5])
print('Массив: ',arr)
variance = np.var(arr)
std_dev = np.std(arr)
print('\n')
print('Дисперсия массива: ',variance)
print('Стандартное отклонение массива: ',std_dev)

arr1 = np.array([[2,5,9],[3,8,4],[4,6,7]])
print('\n')
print('Массив 2: ',arr1)
result1 = np.std(arr1,axis = 0)
result2 = np.std(arr1,axis = 1)
print('Стандартное отклонение массива 2 по строкам: ',result1)
print('Стандартное отклонение массива 2 по столбцам: ',result2)
