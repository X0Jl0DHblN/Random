import numpy as np
import matplotlib.pyplot as plt

p = [f'p{i}' for i in range(5)]
y1 = [10,20,32,13,25]
y2 = [17,15,23,21,27]
width = 0.5
x = np.arange(len(p))
fig,ax = plt.subplots()
ax.set_xticks(x)
ax.set_xticklabels(p)
r1 = ax.bar(x - width/2, y1, width, label = 'y1')
r2 = ax.bar(x + width/2, y2, width, label = 'y2')
ax.legend()
plt.show()
