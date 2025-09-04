N = int(input('Ввведите число: '))
Sum = 0
while N > 0:
    ost = N % 10
    Sum = Sum + ost
    N = N // 10
print(Sum)