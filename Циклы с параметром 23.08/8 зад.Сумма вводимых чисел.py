print()
print('---Сумма вводимых чисел---')

Sum = 0

N = int(input('Количество вводимых значений: '))

for i in range(N):
    a = (int(input('Введите значение: ')))
    Sum += a
    if Sum > 100:
        print()
        print('Сумма чисел', Sum)
        print('Достаточно')
        print('Количество введенных значений:', i)
        print('Число превышающее 100:', Sum % 100)