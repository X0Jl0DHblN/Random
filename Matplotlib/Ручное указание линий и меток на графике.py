import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y1 = [2, 4, 7, 3, 10]
y2 = [i*1.3+1 for i in y1]
y3 = [i*1.3+1 for i in y2]
y4 = [i*1.3+1 for i in y3]

line1 = plt.plot(x,y1,'o-k')
line2 = plt.plot(x,y2,'x-.b')
line3 = plt.plot(x,y3,'*--g')
line4 = plt.plot(x,y4,'+-.c')
plt.legend((line2,line1,line4,line3),['График y2','График y1','График y4','График y3'])
plt.show()