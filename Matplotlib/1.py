import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10,10,50) # формирование значений переменных Х 
print(x)
y1 = x*2+1
y2 = [i**2 for i in x]
plt.title('График линейной зависимости') # заголовок графика
plt.xlabel('Ось абсцисс Х') # ось абсцис
plt.ylabel('Ось ординат У') # ось ординат
plt.grid() # отображение сетки(разметки) на графике
plt.plot(x,y1,'r--') # построение графика, 3 параметр визуальное оформление
plt.show()