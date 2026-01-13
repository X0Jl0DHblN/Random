import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

data = np.random.normal(loc = 0, scale = 1, size = 10000)
print(data)
# =============================================================================
# plt.plot(data)
# =============================================================================
plt.hist(data, bins = 50, density = True, alpha = 0.7, label = 'n = 10000')
x = np.linspace(-4,4,1000)
# =============================================================================
# plt.plot(x, norm.pdf(x, loc = 0, scale = 1))
# =============================================================================
y = norm.pdf(x, loc = 0, scale = 1)
plt.plot(x,y, 'r-',linewidth = 2, label = 'Теоретическая кривая (N(0.1))')

plt.legend()
plt.show()