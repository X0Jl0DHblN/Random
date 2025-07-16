print('Задача 144, поиск минимального значения списка')


A = [int(input('Введите значение: ')) for i in range(5)]
print(A)
 
Min = A[0] 

for x in A: 
    if x < Min:
        Min = x
print('Минимальное значение списка А, равно',Min)        


print('Заполнение списка случайными числами')

from random import*

A = [' '] * 10
for i in range(10):
    A[i] = randint(1,10)
print(A) 


B = [randint(10,100) for i in range(10)]
print(B)  