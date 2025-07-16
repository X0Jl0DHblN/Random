print('Задача 146, поиск среднего арифметического не нулевых элементов списка')


N = int(input('Введите количество элементов списка'))
Sum = 0
A = [' ']*N
for i in range(N):
    A[i] = int(input('После ввода каждого числа нажмите <Enther>'))
print(A)    

total = 0
for i in A:
    total = total + i
print('Сумма элементов списка =', total)    

count = 0
for i in A:
    if i == 0:
        count += 1
quantity = int(len(A) - count) 
print('Количество не нулевых елементов списка =',quantity)

average = total / quantity

print('Среднее арифметическое списка =',average)






