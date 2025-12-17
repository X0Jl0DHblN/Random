import numpy as np
data = ([2, 5, 7, -1000, 9, 11])
# Создани маски в ручную
masked_data = np.ma.masked_equal(data, -1000) #маскирование элемента массива равного -1000
print(masked_data)