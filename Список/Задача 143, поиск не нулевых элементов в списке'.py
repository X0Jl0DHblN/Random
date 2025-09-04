print('Задача 143, поиск не нулевых элементов в списке')


A = [' ']*5
for i in range(5):
    print('A[{}] ->'.format(i), end = '')
    A[i] = int(input('После ввода каждого числа нажмите <Enther>'))
print(A)    
    
   
count = 0
for x in A:
    if x != 0:
        count += 1
print('В массиве',count,'не нулевых элемента')        
        
        