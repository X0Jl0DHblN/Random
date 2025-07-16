print('Сортировка списка по возрастанию')

from random import*

N = int(input('Введите количество элементов списка: '))
print()
A = [randint(1,100) for i in range(N)]
print(A) 

for i in range(N - 1):
    for j in range(N - 2, i - 1, -1):
        if A[j] < A[j+1]:
            A[j],A[j+1] = A[j+1],A[j]

print()            
print('Отсортированный список')
print()
print(A) 