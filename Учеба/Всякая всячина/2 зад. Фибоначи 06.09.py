
 
N = int(input('Введите количество чисел ряда Фобиначи: '))
F1 = F2 = 1 
print(F1, F2, end=' ')
 
for i in range(2, N):
    F1, F2 = F2, F1 + F2
    print(F2, end=' ')