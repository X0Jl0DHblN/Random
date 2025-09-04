print('Задача 152, проверка элементов списка на одинаковые значения')


N = int(input('Введите количество элементов списка: '))
A = [int(input('Введите значение: ')) for i in range(N)]
print(A)
 
flag = 0

for i in range(0,N-2):
    for j in range(i+1,N-1):
        if A[i] == A[j]:
            flag = 1
if flag == 1:
    print('Элементы списка имеют одинаковые значения')
else:
    print('Элементы списка уникальны')        
    
    
    
  