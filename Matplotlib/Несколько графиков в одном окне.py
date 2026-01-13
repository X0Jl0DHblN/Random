import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y1 = [2, 7, 3, 5, 12]
y2 = [i*1.3 + 1 for i in y1]
y3 = [i*1.3 + 1 for i in y2]
y4 = [i*1.3 + 1 for i in y3]

plt.figure(figsize = (20,20))
plt.subplot(4,1,1)
plt.plot(x,y1, '-',color = 'red')
plt.title('График Y1')
plt.ylabel('Y1')
plt.grid(True)

plt.subplot(4,1,2)
plt.plot(x,y2, '-',color = 'blue')
plt.title('График Y2')
plt.ylabel('Y2')
plt.grid(True)

plt.subplot(4,1,3)
plt.plot(x,y3, '-',color = 'brown')
plt.title('График Y3')
plt.ylabel('Y3')
plt.grid(True)

plt.subplot(4,1,4)
plt.plot(x,y4, '-',color = 'magenta')
plt.title('График Y4')
plt.ylabel('Y4')
plt.grid(True)

plt.show()