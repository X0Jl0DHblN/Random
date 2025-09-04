print('Обращение к файлу')

Fin = open('G:\input.txt','r')

list_ = Fin.readline().split()
print(list_)
A = [int(n) for n in list_]
print(A)

Sum = 0
for i in range(len(A)):
    Sum += A[i]
    
print(Sum)    
    