
from random import*

print('*** Случайные числа ***')

N = int(input('Введите количество последовательности чисел: '))

Sum = 0


for i in range(N):
    a = randint(1,10)
    Sum += a
    print(a, end = ' ')
average = Sum / N
print()
print(average)
    