import matplotlib.pyplot as plt
plt.title('Фрукты')
plt.xlabel('Фрукты')
plt.ylabel('Количество')
fruits = ['Яблоко','Апельсин','Груша','Банан']
counts = [36, 25, 43, 16]
plt.bar(fruits, counts)
plt.show()