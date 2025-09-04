print()
print('---Сумма вводимых чисел---')

count = 0
Sum = 0

while Sum < 100:
    a = (int(input('Введите значение: ')))
    count += 1 
    Sum += a
print()
print('Сумма чисел', Sum)
print('Достаточно')
print('Количество введенных чисел:', count)
print('Число превышающее 100:', Sum % 100)