

def Summa(N):
    Sum = 0
    while N!= 0:
        ost = N % 10
        Sum += ost
        N = N // 10
    return Sum
    
n = int(input('Ввведите число: '))
res = Summa(n)
print('Сумма цифр введеннго числа {} равна {}'.format(n,res))