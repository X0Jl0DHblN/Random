print()
print('---Сумма и произведение вводимых чисел---')

Mult = 1
Sum = 0
count = 1
while count < (count + 1):
    N = int(input('Введите число: '))
    if N <= 1000000:
       count += 1
       Sum = Sum + N
       Mult = Mult * N
       print('Сумма введенных чисел равна:', Sum)
       print('Произведение введенных чисел равно:', Mult)  
