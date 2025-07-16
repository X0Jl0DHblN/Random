print('Функция расчета средней арифметической введенной последовательности')

N = int(input('Введите количество цифр: '))

Sum = 0

for i in range(N):   
    x = int(input('Введите цифру и нажмите Enter: '))
    Sum += x 
def average(S,n):
    Sr = S / n
    return Sr

Mean = average(Sum,N)
print('Среднее арифметическое введенной последовательности равняется:',Mean)