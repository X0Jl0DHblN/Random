print(' ')

n = int(input('Введите число: '))

n = bin(n)[2:]
n = int(n)
print(n)

def SUM_N(N):
    Sum = 0
    while N > 0:
        ost = N % 10
        Sum = Sum + ost
        N = N // 10
    return Sum

r = SUM_N(n)

if r % 2 == 0:
    R = str(n) + str(0)*2
else:
    R = str(n) + str(10)
print(R)    
print(int(R, 2))    

Num = int(input('Введите проверочное число: ')) # 43