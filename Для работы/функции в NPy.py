import numpy as np
from math import*

print('\n')
x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print('\n')
print(y)
z = np.maximum(x,y)
print('\n')
print(z)
print('\n')
print(abs(x))
# =============================================================================
# print(fabs(x))
# =============================================================================


print('\n')

c = np.log2(1/16) # ф-ция логарифма
print(c)

print(np.sign(x))

print('\n')

print(np.ceil(-2.5))   #наименьшее целое большее число
print(np.floor(-2.5))   #наибольшее целое наименьшее число
print('\n')
print(np.ceil(x)) #наименьшее целое большее число
print(np.floor(x)) #наибольшее целое наименьшее число
print('\n')
print(np.rint(x)) #округление к ближайшему целому числу
print('\n')
print(np.modf(-2.5)) # возвращает дробную и целую часть
print('\n')
print(np.sin(pi/2))# возвращает значения тригонометрической функции
print('\n')
print(np.cosh(2))# 
print('\n')
print(np.arcsin(0.5))
print(np.arccosh(3.776))