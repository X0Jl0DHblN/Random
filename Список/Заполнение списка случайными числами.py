print('Заполнение списка случайными числами')

from random import*

A = [' '] * 10
for i in range(10):
    A[i] = randint(1,10)
print(A) 


B = [randint(10,100) for i in range(10)]
print(B)   

