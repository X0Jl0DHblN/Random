import matplotlib.pyplot as plt


x = [5.5,10.5,15.5,20.5,25.5,30.5,35.5]
y = [6, 8, 15, 40, 16, 8, 7]
plt.plot(x, y, 'o-r', label = 'line1')
plt.legend(loc = 'center')
plt.show()