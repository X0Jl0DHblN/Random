import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0,5,0.01)
y = np.cos(x*np.pi)

#Маскируем значения точек "У" удовлетворяющие условию y<0.5

y_masked = np.ma.masked_where(y < -0.0, y)

plt.ylim(-1,1) # лимттированные значения оси У

plt.plot(x,y_masked, linewidth = 4)
plt.show()
