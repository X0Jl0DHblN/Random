import matplotlib.pyplot as plt
import numpy as np

np.random.seed(123)
x = np.random.randint(-5,5,50)
y = np.random.randint(0,10,50)
z = np.random.randint(-5,5,50)
s = np.random.randint(10,100,20)
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')
ax.scatter(x,y,z,s = 15, c = 'r')
plt.show()