
print('Рекурсивное вычисление чисел Фибоначи')

def fibRec(N):
    if N < 3:
        return 1
    return fibRec(N - 1) + fibRec(N - 2)


N = int(input('Введите число: '))

print(fibRec(N))