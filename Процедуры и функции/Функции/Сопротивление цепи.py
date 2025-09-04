print('Сопротивление цепи')

R1 = int(input('Введите величину первого сопротивления: '))
R2 = int(input('Введите величину второго сопротивления: '))
Type = int(input('Введите тип сопротивления: 1 - последовательное, 2 параллельное'))

def resist(a,b,c):
    if c == 1:
        R = a + b
    elif c == 2:
        R =a*b/(a +b)
    else:
        R = -1
    return R

R = resist(R1,R2,Type)

if R != -1:
    print('Сопротивление цепи равно:', resist(R1,R2,Type))  
else:
    print('Тип цепи указан не верно')

        