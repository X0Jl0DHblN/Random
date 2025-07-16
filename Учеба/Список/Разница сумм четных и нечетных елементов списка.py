print('Разница сумм четных и нечетных елементов списка')

N = int(input('Введите количество елементов списка: '))
A = [int(input('Введите число и нажмите <Enther>: ')) for i in range(N)]
print(A)

even = 0
not_even = 0
for x in A:
    if x % 2 == 0:
        even += x
    else:
        not_even += x
print(even,'Сумма четных елементов') 
print(not_even,'Сумма не четных елементов')      
difference = even - not_even
if difference > 0:
    print('Разница между суммой четных и не четных елементов списка составляет: ', difference)
else:
    print('На {} сумма нечетных элементов списка, больше суммы четных елементов'.format(difference * (-1))) 