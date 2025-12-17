import numpy as np


arr = np.array ([1,2,3,4,5])
#Создаём маску по условию arr > 3
masked_array = np.ma.masked_where(arr > 3, arr )# маскирование элементов массива arr, которые больше 3
print(masked_array)