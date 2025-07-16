print('Сумма и среднее арифметическое вводимой последовательности')

Sum = 0
count = 0
N = 1

while N != 0:
    N = int(input('Введите число: '))
    if N > 0:
        Sum = Sum + N
        count += 1
average = Sum / count   
print('Сумма введенных чисел:',Sum)  
print('Среднее арифметическое введенной последовательности: {:0.2}'.format(average))  
    