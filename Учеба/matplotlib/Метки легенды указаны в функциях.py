import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y1 = [2, 4, 7, 3, 10]
y2 = [i*1.3+1 for i in y1]
y3 = [i*1.3+1 for i in y2]
y4 = [i*1.3+1 for i in y3]

plt.plot(x,y1,'o-r', label = 'График у1')
plt.plot(x,y2,'x-.b', label = 'График у2')
plt.plot(x,y3,'*--k', label = 'График у3')
plt.plot(x,y4,'+-.m', label = 'График у4')
plt.legend()
plt.show()