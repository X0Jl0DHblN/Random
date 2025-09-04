print('Функция вычисления минимального из 3-х введенных чисел')
print()


def Min_2(a,b): 
    if a < b:
        Min = a
    else:
        Min = b
    return Min  

def Min_3(a,b,c):
    return Min_2(Min_2(a,b),c)
    
    

a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))

Min_N = Min_3(a,b,c)
    
print('Минимальное число из введенных чисел {},{},{} равно {}:'.format(a,b,c,Min_N))  



    