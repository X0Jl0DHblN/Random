import numpy as np
import matplotlib.pyplot as plt

normal_data = np.random.normal(loc = 0, scale = 1, size = 100)
print(normal_data)

plt.plot(normal_data)
plt.show()