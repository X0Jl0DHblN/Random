print('Функция вычисления минимального введенного числа')
print()


def Min_num(n): 
    MinF = n
    if n > MinF:
        MinF = MinF
    if n < MinF:
        MinF = n
    return MinF  
  

for i in range(5):
    N = int(input('Введите число: '))
    MinN = 0
    MinN = Min_num(N)
    
print('Минимальное число из введенной последовательности:', MinN)        