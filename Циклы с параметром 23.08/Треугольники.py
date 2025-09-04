print()  
print ('---Треугольник 1---')
H = int(input('Высота треугольника: '))
Sim = input('Введите символ: ')
print()
for i in range (H + 1):
    A = Sim * i
    print(A)
    
print('-----------------------')   
print() 
print ('---Треугольник 2---')
print()    
H = int(input('Высота треугольника: '))
Sim = input('Введите символ: ')
print()
for i in range (H + 1):
    A = Sim * (H - i)
    print(A)

print('-----------------------')   
print() 
print ('---Треугольник 3---')
print()
H = int(input('Высота треугольника: '))
Sim = input('Введите символ: ')
print()
for i in range (H + 1):
    A = (H-i) * Sim
    print(i * ' ' + A)
    
    
print('-----------------------')   
print() 
print ('---Треугольник 4---')
print()
H = int(input('Высота треугольника: '))
Sim = input('Введите символ: ')
print()    
for i in range (H + 1):
    A = Sim * i
    print((H - i) * ' ' + A)