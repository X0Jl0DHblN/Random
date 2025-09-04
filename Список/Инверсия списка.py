print('Инверсия списка')

N = int(input('Введите количество элементов списка: '))

A = [int(input('Элемент списка: ')) for i in range(N)]
print(A)

for i in range(0,N//2):
    X = A[i]
    A[i] = A[N-1-i]
    A[N-1-i] = X
    
print(A)