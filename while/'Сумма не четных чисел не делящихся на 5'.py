print('Сумма не четных чисел не делящихся на 5')

N = 1
count = 0
print()
while N != 0:
    N = int(input('Введите N: '))
    if N % 2 !=0 and N % 5 ==0:
        count += 1
print('Количество введенных цифр не делящихся на 5,', count)        