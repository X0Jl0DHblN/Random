import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

np.random.seed(10)
x = np.random.rand(100)
y = np.random.rand(100)
z = np.random.rand(100)

# Create a figure and 3D axis
fig = plt.figure(figsize=(5,8))
ax = fig.add_subplot(111, projection='3d')

# Create scatter plot
ax.scatter3D(x, y, z, color='g', marker='D')

# Labels
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')
ax.set_title('Basic 3D Scatter Plot')


plt.show()