print('Рекурсия цифр Фибоначчи')

N = int(input('Введите число: '))

def F(n):
    if n < 3:
        return 1
    else:
        return F(n-1)+F(n-2)
        

for i in range(1, N + 1):
    Res = F(i)
    print(Res)
    