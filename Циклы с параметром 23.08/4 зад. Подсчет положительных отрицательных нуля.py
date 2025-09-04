
print('---Ввод нескольких чисел и подсчет четных---')
print()
N = int(input('Введите количество цифр в последовательности: '))

count_pol = 0
count_otr = 0
count_0 = 0

for i in range(N):
    a = int(input('Введите число нажмите <Enter>: ')) 
    if 0 < a:
        count_pol +=  1
    elif 0 > a:
        count_otr += 1
    else:
        count_0 += 1
print()
print('Количество положительных чисел в последовательности', count_pol)
print('Количество отрицательных чисел в последовательности', count_otr)
print('Количество нулей в последовательности', count_0)