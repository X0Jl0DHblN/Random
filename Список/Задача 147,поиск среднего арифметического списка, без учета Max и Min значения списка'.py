print('Задача 147,поиск среднего арифметического списка, без учета Max и Min значения списка')

N = int(input('Введите количество элементов списка: '))
A = [int(input('Введите значение: ')) for i in range(N)]
print(A)
 
Min = A[0] 
for i in A: 
    if i < Min:
        Min = i
print('Минимальное значение списка А, равно',Min) 

Max = A[0]       
for i in A: 
    if i > Max:
        Max = i
print('Максимальное значение списка А, равно',Max) 

total = 0
for i in A:
    total = total + i
print('Сумма элементов списка, без Max и Min =', total - Max - Min)    

average = total / N

print('Среднее арифметическое списка без учета Max и Min =',average)