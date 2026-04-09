import matplotlib.pyplot as plt

# Данные для диаграммы
Dokes = ['A', 'B', 'C', 'D', 'E']
values = [25, 40, 30, 55, 15]

# Создание диаграммы
plt.figure(figsize=(10, 6))
plt.bar(Dokes, values)
plt.title('Нагрузка на транспортные доки')
plt.xlabel('Доки')
plt.ylabel('Объём')
plt.show()