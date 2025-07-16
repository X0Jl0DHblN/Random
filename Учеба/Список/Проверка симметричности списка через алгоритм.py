print('Проверка симметричности списка через алгоритм')

N = int(input('Введите количество елементов списка: '))
A = [int(input('Введите число и нажмите <Enther>: ')) for i in range(N)]
print(A)


y = 0
flag = 0
if len(A) % 2 == 0:
    for i in range(int(len(A)/2)):
        if A[i] == A[-1 + y]: 
            y -=1
            flag = 0            
        else:
            flag = 1            
if len(A) % 2 == 1:                    
    for i in range(int(len(A)/2)):
        if A[i] == A[-1 + y]:
            flag = 0
            y -=1
        else:
            flag = 1
print(flag)                      
if flag == 0:
    print('Элементы списка симметричны') 
else:
    print('Элементы списка не симметричны')           
            
            
        