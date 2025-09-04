print('Функция определения минимального из введенных чисел')

N = int(input('Введите количество цифр: '))



for i in range(N):
    min_dig = 0
    max_dig = 0
    Dig = int(input('Введите цифру и нажмите Enter: '))
    if Dig > max_dig: 
        max_dig = Dig
    else:
        min_dig = Dig

    


print('Минимальное число из введенной последовательности равняется :',min_dig, max_dig)