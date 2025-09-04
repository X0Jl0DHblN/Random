print()
print('---Поиск НОД----')
 
Num1 = int(input('Ввведите число 1: '))
Num2 = int(input('Ввведите число 2: '))
while Num1 != 0 and Num2 != 0:
    if Num1 > Num2:
        Num1 = Num1 - Num2
    else:
        Num2 = Num2 - Num1
print('Наибольший общий делитель для ввденных чисел:', Num1)