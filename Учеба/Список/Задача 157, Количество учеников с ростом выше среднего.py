print('Задача 157, Количество учеников с ростом выше среднего')

N = int(input('Введите количество учеников: '))
A = [int(input('Введите рост ученика (см) и нажмите <Enther>: ')) for i in range(N)]
print(A)
 
total = 0
for x in A:
    total = total + x
average = total / N    
print('Средний рост учеников в классе =', average) 

count = 0     
for b in A: 
    if b > average:
        count += 1
print('Количество учеников с ростом выше среднего =',count) 

   



