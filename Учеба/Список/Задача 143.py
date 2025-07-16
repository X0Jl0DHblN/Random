print('Задача 143, поиск не нулевых элементов в списке')

count = 0
A = [' ']*5
for i in range(5):
    print('A[{}] ->'.format(i), end = '')
    A[i] = int(input('После ввода каждого числа нажмите <Enther>'))
print(A)    
    
   
count = 0
for i in A:
    if i == 0:
        count += 1
print('В массиве', len(A) - count,'не нулевых элемента')        
        
        