print('Рекурсия суммы чисел числа')

N = int(input('Введите число:  '))

def F(n):
    if n == 0:
        return 0
    digit = n % 10
    Sum = F(n // 10)
    return Sum + digit 
   
res = F(N)       
print(res)

















