#a = 123 % 10
#b = 123 // 10
#print(a,b)

print('Реверс значений введенного числа')

def numReverse(n):
    a = 0
    while n > 0:
        a = a * 10 + n % 10
        n = n // 10
        #print(a,n)
    return a
 
N = int(input('Введите число: '))
N_rev = numReverse(N)
print('Зеркальным отображением введенного числа {} является {}'.format(N,N_rev))