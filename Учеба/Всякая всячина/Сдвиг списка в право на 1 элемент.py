print('Сдвиг списка в право на 1 элемент')

N = int(input('Введите количество элементов списка: '))

A = [int(input('Элемент списка: ')) for i in range(N)]
print(A)

X = A[N-1]

print('X=',X)
for i in range(1,N):
    A[N-i] = A[N-1-i]
    print(A[i])
A[0] = X   

print(A)         

