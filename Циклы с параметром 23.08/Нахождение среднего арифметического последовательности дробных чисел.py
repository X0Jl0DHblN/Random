print('Нахождение среднего арифметического последовательности дробных чисел')
print('После каждого числа нажимайте <Enter>')
N = int(input('Введите количество чисел: '))
Sum = 0
count = 0

for i in range(N):
    a = float(input('Введите число: '))
    Sum += a
    count += 1
    average = Sum / count
    print('Введено чисел', count, 'Сумма: ', Sum, 'Среднее арифметическое: ', average)
    



