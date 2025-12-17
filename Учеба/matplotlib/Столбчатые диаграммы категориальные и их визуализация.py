import numpy as np
from random import*
import matplotlib.pyplot as plt


np.random.seed(123)
x = [f'x{i}' for i in range(5)]
y = np.random.randint(0,10,len(x))
plt.bar(x,y,width = 0.1, alpha = 0.6, bottom = 5, color = 'y', edgecolor = 'r', linewidth = 8)
plt.show