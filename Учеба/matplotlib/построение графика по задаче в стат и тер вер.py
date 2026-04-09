import matplotlib.pyplot as plt


xi = [2.5, 7.5, 12.5, 17.5, 22.5, 27.5]
ni = [133, 45, 15, 4, 2, 1]
# Создание диаграммы
plt.figure(figsize=(10, 5))
plt.bar(xi, ni)
plt.show()