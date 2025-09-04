print('Применение ЛФ в функции reduce()')

from functools import reduce

print(reduce(lambda x,y: y * x, range(1,6),1))
