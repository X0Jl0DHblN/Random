print('Индекс первого и последнего элемента списка, равный максимальному значению списка')

N = int(input('Введите количество элементов списка: '))
A = [int(input('Введите значение: ')) for i in range(N)]
print(A)


Max = A[0]       
for i in A: 
    if i > Max:
        Max = i
print('Максимальное значение списка =',Max)        
for j in range(N):
    if A[j] == Max:
        print('A[',j,']=', A[j], sep='')




    