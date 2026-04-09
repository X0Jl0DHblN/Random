import matplotlib.pyplot as plt
import numpy as np

u,v = np.mgrid[0:2*np.pi:30j, 0:np.pi:10j]
x = np.cos(u) * np.sin(v)
y = np.sin(u) * np.sin(v)
z = np.cos(v)
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.plot_wireframe(x,y,z)
ax.legend()
plt.show()