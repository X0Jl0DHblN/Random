import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = np.linspace(-np.pi,np.pi,50)
y = x
z = np.cos(x)
fig = plt.figure()
ax = fig.add_subplot(111,projection = '3d')
ax.plot(x,y,z, label = 'Параметрическая кривая', marker = 'o', ms = 2)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend()
plt.title('3D Параметрическая кривая, z = cos(x), y = x')
plt.show()