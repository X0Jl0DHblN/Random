print('вычисление чисел Фибоначи методом мемоизации')


Fib = {1:1, 2:1}

def fibMemo(N):
    if N in Fib:
        return Fib[N]
    Fib[N] = fibMemo(N-1) + fibMemo(N-2)
    return Fib[N]

N = int(input('Введите число: '))

print(fibMemo(N))