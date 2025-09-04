import numpy as np

data = [3,7,5,8,12,13,18,14,21,45]
data = sorted(data)
print(data)
print('\n')
Q1 = np.percentile(data,25)
Q3 = np.percentile(data,75)
print('Q1 = ',Q1)
print('Q3 = ',Q3)