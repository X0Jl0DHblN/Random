import matplotlib.pyplot as plt


x = [1,4,11,16,23]
y1 = [2,8,3,6,13]
y2 = [4,3,2,8,15]
plt.figure(figsize=(14,9))
plt.plot(x,y1,'o-r', alpha = 0.6, label='1-й график', lw = 5, mec = 'b', mew = 2, ms = 10, mfc = 'y')
plt.plot(x,y2,'v-.', label = '2-й график', linewidth = 2, markeredgecolor = 'r', markeredgewidth =3, markersize = 12)
plt.legend()
plt.grid(True)
plt.show()