import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy import stats

np.random.seed(46)  # точка генерации псевдослучайных чисел
mu = 10   # Мат. ожидание
sigma = 2  # Стандартное отклонение
n = 100      # Размер выборки

data = np.random.normal(mu, sigma, n)

def sepr1():
    print('-' * 50)

def sepr2():
    print('=' * 50)
    

 
print('\n ЛАБОРАТОРНАЯ РАБОТА')
print('\n Проверка гипотезы о норомальном распределении данных')
sepr2()
print('\n Набор данных для исследования:')    
sepr1()
print(data)
sepr2()
print('\n Полученные статистические характеристики:')
sepr1()


data_size = len(data)
mean_value = np.mean(data)
median_value = np.median(data)
std_deviation = np.std(data, ddof=1) 
coeff_variation = (std_deviation / mean_value) * 100


print(f"Размер выборки: {data_size}")
print(f"Среднее значение: {mean_value:.4f}")
print(f"Медиана: {median_value:.4f}")
print(f"Стандартное отклонение: {std_deviation:.4f}")
print(f"Коэффициент вариации: {coeff_variation:.2f}%")


plt.figure(figsize=(10, 6))
plt.hist(data, bins= 30, density=True, alpha=0.6, color='skyblue', edgecolor='black')


x = np.linspace(min(data), max(data), 100)
y = norm.pdf(x, mu, sigma)
plt.plot(x, y, 'r-', linewidth=5, label= 'Теоретическая кривая')


plt.title('Гистограмма с нормальной кривой распределения')
plt.xlabel('Значения')
plt.ylabel('Плотность')
plt.legend()
plt.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()

#СТАТИСТИЧЕСКИЕ ТЕСТЫ

ks_stats, ks_p = stats.kstest(data,'norm', args = (np.mean(data), np.std(data)))
print(f'Статистика:{ks_stats:.4f}')
print(f'Значение p_value:{ks_p:.10f}')
print(f"Вывод:{'Нормальное распределение' if ks_p>0.05 else 'не нормальное распределение'}")