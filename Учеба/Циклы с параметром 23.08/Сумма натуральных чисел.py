print('Сумма первых N чисел')

N = int(input('Введите число N: '))
Sum = 0
for i in range(1, N+1):
    Sum = Sum + i
print('Сумма первых', N, 'чисел равна', Sum)    