print('Вычисление факториала числа')

N = int(input('Введите число: '))

def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact

for j in range(1,N+1):
    f = factorial(j)
    print('{:3}{:5}'.format(j,f))

    
    
    
    
    


    