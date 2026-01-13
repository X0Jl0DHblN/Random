import numpy as np
import matplotlib.pyplot as plt

val = [25,16,54,20,37]
labels = ['Audi', 'Toyota', 'BMW', 'Ford', 'lada']
fif,ax = plt.subplots()
ax.pie(val, labels = labels, wedgeprops = dict(width = 0.5, edgecolor = 'k', linewidth = 2, linestyle = '--'))
plt.show()