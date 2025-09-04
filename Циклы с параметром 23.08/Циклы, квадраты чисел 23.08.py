
N = int(input('Введите число N: '))
print('Таблица степеней двойки.')
print('-------------------')


for i in range(N+1):
     print('{:4}   {:8}'.format(i, 2**i))  
