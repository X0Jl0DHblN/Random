import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm


np.random.seed(12)  # точка генерации псевдослучайных чисел
mu = 10.0    # Мат. ожидание
sigma = 0.05  # Стандартное отклонение
n = 100      # Размер выборки

data = np.random.normal(mu, sigma, n)

def sepr1():
    print('-' * 50)

def sepr2():
    print('=' * 50)
    

print()   
print('ЛАБОРАТОРНАЯ РАБОТА')
print()    
print('Проверка гипотезы о норомальном распределении данных')
sepr2()
print()
print('Набор данных для исследования:')    
sepr1()
print(data)
sepr1()

print()
print('Полученные статистические характеристики:')
sepr2()

data_size = len(data)
mean_value = np.mean(data)
median_value = np.median(data)
std_deviation = np.std(data, ddof=1) 
coefficient_variation = (std_deviation / mean_value) * 100


print(f"Размер выборки: {data_size}")
print(f"Среднее значение: {mean_value:.4f}")
print(f"Медиана: {median_value:.4f}")
print(f"Стандартное отклонение: {std_deviation:.4f}")
print(f"Коэффициент вариации: {coefficient_variation:.2f}%")

# ПОСТРОЕНИЕ ГРАФИКА ДЛЯ ВИЗУАЛИЗАЦИИ ДАННЫХ
plt.figure(figsize=(10, 6))

# Построение гистограммы
plt.hist(data, bins= 15, density=True, alpha=0.6, color='skyblue', edgecolor='black')

# Нормальная кривая
x = np.linspace(min(data), max(data), 1000)
y = norm.pdf(x, mu, sigma)
plt.plot(x, y, 'r-', linewidth=2, label=f'Normal (μ={mu:.4f}, σ={sigma:.4f})')

# Настройки графика
plt.title('Гистограмма с нормальной кривой распределения')
plt.xlabel('Значения')
plt.ylabel('Плотность')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
