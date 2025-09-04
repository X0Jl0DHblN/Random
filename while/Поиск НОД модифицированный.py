print()
print('---Поиск НОД модифицированный----')
 
Num1 = int(input('Ввведите число 1: '))
Num2 = int(input('Ввведите число 2: '))
while Num1 != 0 and Num2 != 0:
    if Num1 > Num2:
        Num1 %= Num2
    else:
        Num2 %= Num1
if Num1 != 0:
    print('Наибольший общий делитель для ввденных чисел:', Num1)
else:
    print('Наибольший общий делитель для ввденных чисел:', Num2)            
        
