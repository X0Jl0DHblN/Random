import numpy as np

arr = np.arange(10)
print(arr)
print('\n')
print('Печать индекса 5:',arr[5])
print('\n')
print('Печать среза 5-8:',arr[5:8])
print('\n')
arr[5:8] = 13
print('Замена значений по срезу 5 - 8:',arr)
print('\n')
arr1 = arr[5:8]
print(arr1)
print('\n')
arr1[1] = 1000000
print('\n')
print(arr)
print('\n')
arr1[:] = -10
print(arr)
print('\n')
arr2 = np.arange(9)
print(arr2)
print('\n')
arr3 = arr2.reshape(3,3)
print(arr3)
print('\n')
print('Печать 2-го индекса в двумерном массиве:',arr3[2])
print(arr3[1,2])
print(arr3[1][2])
print('Вторая строка матрицы: ', arr3[1:])
print('Третий столбец матрицы: ', arr3[:2])