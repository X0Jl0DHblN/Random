import matplotlib.pyplot as plt


plt.plot([-3, 0, 5, 7, 12], [1, 6, 3, 11, 2])
plt.xlabel('Ось абсцисс X', fontsize = 16, color = 'red', fontstyle = 'italic', fontweight = 'bold')
plt.title('График', fontsize = 18, color = 'blue', loc = 'center')
plt.text(1,1,'Это ломанная')