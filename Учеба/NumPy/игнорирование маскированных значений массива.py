import numpy as np

data = np.ma.array([1,2,5,100,6,7], mask = [0,0,0,1,0,0])#игнорирование маскированных значений
x = np.ma.mean(data)
print(x)