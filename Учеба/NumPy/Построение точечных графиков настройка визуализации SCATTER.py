import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,5,0.15)
y = np.cos(x)
plt.scatter(x,y, s = 60, c = 'r', marker = 'D', linewidths = 2, edgecolor = 'g')

