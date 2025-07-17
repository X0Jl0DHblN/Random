


N = int(input('Введите размерность списка элементов: '))
A = []

for x in range(N):
    x = int(input('Введите значение: '))
    A.append(x)
A.reverse()
print(A)  

even = []
n_even = []

for x in A:
    if x % 2 == 0:
        even.append(x)
    else:
        n_even.append(x)
        
print(even)   
print(n_even)   
print('Указатели начала и конца четной очереди {}, {}'.format(even[-1],even[0]))  
print('Указатели начала и конца не четной очереди {}, {}'.format(n_even[-1],n_even[0])) 
        