N = int(input('Введите число: '))
 
for i in range(2, N):
    
    if (N % i) == 0:
        print ('Число ', N, 'не простое')
        break
    
    elif (N // i) == 1:
        print ("Число ", N, " простое!")
        break