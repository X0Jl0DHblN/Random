import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y1 = [2, 4, 7, 3, 10]
y2 = [i*1.3+1 for i in y1]
y3 = [i*1.3+1 for i in y2]
y4 = [i*1.3+1 for i in y3]

plt.plot(x,y1,'o-y')
plt.plot(x,y2,'x-.c')
plt.plot(x,y3,'*--g')
plt.plot(x,y4,'+-.m')
plt.legend(['График y1','График y2','График y3','График y4'])
plt.show()