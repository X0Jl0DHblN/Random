from random import*


print('Вычисление среднего значения ряда рандомных чисел')
print()
print('*** Случайные числа ***')
N = int(input('Введите количество чисел в ряду: '))

Sum_a = 0
Sum_b = 0
Sum_c = 0

for i in range(N):
    a = randint(1,10)
    Sum_a += a
    print(a, end = ' ')
print()    
for i in range(N):   
    b = randint(1,10)
    Sum_b += b
    print(b, end = ' ')
print()      
for i in range(N):    
    c = randint(1,10)
    Sum_c += c
    print(c, end = ' ')
print()      
average_a = Sum_a / N
average_b = Sum_b / N
average_c = Sum_c / N   
print('Среднее арифметическое первой последовательности ', average_a) 
print('Среднее арифметическое второй последовательности ', average_b)   
print('Среднее арифметическое третьей последовательности ', average_c)     
