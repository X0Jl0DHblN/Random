print('Заполнение списка вручную с клавиатуры')


#N = 5
#a = [' ']*N
#for i in range(N):
    #a[i] = int(input('Введите значение: '))
#print(a)  


#B = [2*i for i in range(10)]
#print(B)

  

#C = [int(input('Введите значение: ')) for i in range(5)]
#print(C)


A = [' ']*5
for i in range(5):
    print('A[{}] ->'.format(i), end = '')
    A[i] = int(input())
    