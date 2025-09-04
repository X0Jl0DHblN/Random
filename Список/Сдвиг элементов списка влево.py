print('Сдвиг списка влево на 1 элемент')

N = int(input('Введите количество элементов списка: '))

A = [int(input('Элемент списка: ')) for i in range(N)]
print(A)

X = A[0]
#print('X=',X)
for i in range(N-1):
    A[i]=A[i+1]
    print(A[i])
A[4] = X   

print(A)         




