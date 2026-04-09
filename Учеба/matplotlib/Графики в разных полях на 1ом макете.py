import matplotlib.pyplot as plt

x = [1, 3, 5, 7, 9]
y1 = [2, 4, 7, 3, 10]
y2 = [i*1.3+1 for i in y1]
y3 = [i*1.3+1 for i in y2]
y4 = [i*1.3+1 for i in y3]
fig,axs = plt.subplots(2,2,figsize = (14,8))
axs[0,0].plot(x,y1,'-r')
axs[0,1].plot(x,y2,'--b')
axs[1,0].plot(x,y3,'-.g')
axs[1,1].plot(x,y4,':y')
plt.show()
