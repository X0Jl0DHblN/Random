import numpy as np
from scipy import stats

data1 = np.array([[1,2,3],[1,3,3],[2,2,3]])
print(data1)

Moda1 = stats.mode(data1,axis = 1)
print('Moda по столбцам = ', Moda1.mode)
print('Количество = ',Moda1.count)
