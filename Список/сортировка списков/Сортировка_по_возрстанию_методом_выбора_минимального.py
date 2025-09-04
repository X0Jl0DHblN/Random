print('Сортировка списка по возрастанию методом выбора минимального')

from random import*

N = int(input('Введите количество элементов списка: '))
print()
A = [randint(1,100) for i in range(N)]
print(A)

for i in range(len(A)):
    index_Min = i
    for j in range(i + 1,len(A)):
        if A[j] < A[index_Min]:
            index_Min = j
    if index_Min != i:
       A[i],A[index_Min] = A[index_Min],A[i]

print()            
print('Отсортированный список')
print()
print(A)             