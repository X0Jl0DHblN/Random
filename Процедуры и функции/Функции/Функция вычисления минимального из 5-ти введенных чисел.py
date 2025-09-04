print('Функция вычисления минимального из 5-ти введенных чисел')
print()


def Min_2(a,b): 
    if a < b:
        Min = a
    else:
        Min = b
    return Min

def Min_3(a,b,c):
    return Min_2(Min_2(a,b),c)    

def Min_5(a,b,c,d,e):
    return Min_2(Min_2(Min_2(Min_2(a,b),c),d),e)
    
def Min_5(a,b,c,d,e):
    return Min_2(Min_2(Min_3(a,b,c),d),e)

a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = int(input('Введите число 3: '))
d = int(input('Введите число 4: '))
e = int(input('Введите число 5: '))

Min_N = Min_5(a,b,c,d,e)
    
print('Минимальное число из введенных чисел {},{},{},{},{} равно {}:'.format(a,b,c,d,e,Min_N))