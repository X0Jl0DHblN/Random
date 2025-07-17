print('Реверс списка')

N = int(input('Введите количество елементов списка: '))
A = [int(input('Введите число и нажмите <Enter>: ')) for i in range(N)]
print(A)

print(A[::-1])

