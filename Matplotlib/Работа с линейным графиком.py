import matplotlib.pyplot as plt

x = [1, 5, 10, 15, 20]
y = [2, 7, 3, 5, 12]

line = plt.plot(x, y, label = 'График функции')
plt.setp(line, linestyle = 'dashdot',color = 'blue', linewidth = 3)
plt.title('Точечный график', fontsize = 16)
plt.xlabel('Ось Х', fontsize = 12, color = 'r')
plt.ylabel('Ось Y', fontsize = 12, color = 'r')
plt.legend()
plt.grid(True)
plt.text(14,4,'График ломанной', fontweight = 1000, color = 'magenta')
plt.show()

