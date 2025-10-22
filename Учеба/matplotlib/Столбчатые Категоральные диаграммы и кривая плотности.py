import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

plt.title('Диаграмма')
data_X = [1.5, 4.5, 7.5, 10.5, 13.5, 16.5, 19.5, 22.5, 25.5, 28.5]
data_N = [1,3,4,6,11,10,7,5,2,1]
# =============================================================================
# plt.xlabel('1.5,   4.5,   7.5,   10.5,   13.5,   16.5,   19.5,   22.5,   25.5,   28.5')
# =============================================================================
x = np.linspace(0,30,1000)
plt.bar(data_X, data_N)
y = norm.pdf(x, loc = 15, scale = 0.08)
plt.plot(x, y,'r-',linewidth = 2, label='Теоретическая кривая N')
plt.legend()
plt.show()
