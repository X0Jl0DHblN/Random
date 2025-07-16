N = int(input('Введите количество чисел ряда Фобиначи: '))
F1 = 1
F2 = 1
print(F1, F2, end = ' ')
for i in range(N):
    print(F1 + F2, end = ' ')
    F2 =  F1 + F2
    F1 = F2 - F1

    