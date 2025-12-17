import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0, 10)
y = x
plt.step(x,y, 'r-o', where = 'mid')
plt.grid()
plt.show()

