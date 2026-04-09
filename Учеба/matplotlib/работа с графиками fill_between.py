import matplotlib.pyplot as plt
import numpy as np


x = np.arange(0,5.0,0.001)
y = np.cos(x * np.pi)
plt.plot(x, y, 'r')
plt.grid(True)
#plt.fill_between(x,y,where = (y>0.6)|(y<-0.6))# заливка центра дуг
#plt.fill_between(x,0.5,y,where = (y>0.5))# заливка пиков графика
plt.fill_between(x,y,where = y>0, color = 'r', alpha = 0.8)#заливка пиков в графике выше 0
plt.fill_between(x,y,where = y<0, color = 'g', alpha = 0.2)#заливка графика ниже 0
plt.show()