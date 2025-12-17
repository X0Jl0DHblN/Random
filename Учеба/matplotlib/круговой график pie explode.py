import numpy as np
import matplotlib.pyplot as plt

num = (24,16,57,21,36)
lab = ['Яблоки','Апельсин', 'Груши', 'Орехи', 'Вишня']
fig,ax = plt.subplots()
ax.pie(num, labels = lab, explode = [0.1,0,0.1,0,0])
ax.axis('Значение')
plt.show()