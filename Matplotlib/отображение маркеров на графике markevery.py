import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5]
y = [7,4,1,2,8]
plt.plot(x, y, marker = 'o', color = 'r')
plt.show()

x = np.arange(0,5.0,0.05)
y = np.cos(x * np.pi)
plt.plot(x,y,marker ='^', color = 'g', markevery = 0.4)
plt.show()
