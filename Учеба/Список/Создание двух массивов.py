print('Создание двух массивов')

N = int(input('Введите количество елементов списка: '))
A = [int(input('Введите число и нажмите <Enther>: ')) for i in range(N)]
print(A)

B = [0]*N
count  = 0
for i in range(N):
    if A[i] > 0:
        B[count] = A[i]
        count += 1
for i in range(count):
    print(B[i], end = ' ')        
        
        
        