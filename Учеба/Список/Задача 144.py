print('Задача 144')


A = [int(input('Введите значение: ')) for i in range(5)]
print(A)
 
Min = A[0] 

for i in A: 
    if i < Min:
        Min = i
print('Минимальное значение списка А, равно',Min)        