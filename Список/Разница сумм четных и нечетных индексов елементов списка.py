print('Разница сумм четных и нечетных индексов елементов списка')

N = int(input('Введите количество елементов списка: '))
A = [int(input('Введите число и нажмите <Enther>: ')) for i in range(N)]

even = 0
not_even = 0
for i in range(len(A)):
    print('A[',i,']=', A[i], sep='')
    
for i in range(N):
    if i % 2 == 0:
        even += A[i]
    else:
        not_even += A[i]   
difference = even - not_even
print(even,'Сумма элементов списка с четными индексами')
print(not_even,'Сумма элементов списка с четными индексами')
print(difference)
if difference > 0:
    print('Разница между суммой с четными и не четными индексами елементов списка составляет: ', difference)
else:
    print('На {} сумма с нечетными индексами элементов списка, больше суммы с четными индексами елементов'.format(difference * (-1))) 