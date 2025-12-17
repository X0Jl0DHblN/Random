import matplotlib.pyplot as plt
import numpy as np

x= np.arange(0,10.5,0.5)
y = ([(-0.2) * i**2 +2*i for i in x])
plt.stem(x,y, linefmt = 'r-.', markerfmt = '*',basefmt = '--', bottom = 1)
plt.grid()
plt.show()