m=int(input('Введете число строк -> '))
n=int(input('Введете число столбцов -> '))
for i in range(1,m+1):
    if i%2==0:
        print(' ',end='')
    print('*'*n)
