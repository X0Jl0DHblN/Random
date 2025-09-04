print('Сортировка слиянием')
 
from random import*
 
N = int(input('Введите количество элементов списка: '))
print()
A = [randint(1,100) for i in range(N)]

print(A) 

 
def mergeSort(A):
    if len(A) <= 0:
        return A
    mid = len(A) // 2
    L = mergeSort(A[:mid])
    R = mergeSort(A[mid:])
    return merge(L,R)
 
def merge(A,B):
    C = []
    while A and B:
        if A[0] <= B[0]:
            C.append(A.pop(0))
        else:
            C.append(B.pop(0))
        return C + A + B
Sort_A = mergeSort(A)
print(Sort_A)