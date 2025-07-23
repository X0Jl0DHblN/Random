import numpy as np

data = np.array([4,8,6,5,3,2,8,9,2,5])
print('Размерность :', data.shape)
print('Тип данных: ', data.dtype)
data_s = np.sort(data)
print(data_s)


print('\n')
arr = data.reshape(2,5)
print(arr)
print('\n')
print('Максимальное значение массива D1: ', data.max())
print('Максимальное значение массива D2: ', arr.max())
print('Максимум в строках массива D2 через метод: ', arr.max(axis = 1))
print('Максимум в строках массива D2 по функции: ', np.max(arr,axis = 1))

print('\n')



print('Уникальные хначения массива',np.unique(data))
print('Медиана массива',np.median(data))
print('Среднее значение массива',np.mean(data))
print('\n')
print('Среднее значение массива D1 через метод', data.mean())
print('Среднее уникальных значений массива D1 через функцию ', np.mean(np.unique(data)))

print('\n')
values,counts = np.unique(data, return_counts=True)
print('Массив уникальных значений',values)
print('Частота вхождения уникальных значений',counts)
