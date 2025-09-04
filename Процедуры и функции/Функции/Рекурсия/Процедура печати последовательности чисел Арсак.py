import sys
print('Процедура печати последовательности чисел Арсак')

N = int(input('Введите число: '))

def F(n):
    print(n)
    if n == 1:
        sys.exit()         
    if n % 2 == 0:
        return F(n//2)
    else:
        return F(3 * n + 1)

F(N)        
 
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        