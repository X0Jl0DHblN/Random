from random import*


a = randint(1,6)
b = randint(1,6)
c = randint(1,6)
A = a*100+b*10+c
B = A**2
print('Первая цифра: ',a)
print('Вторая цифра: ',b)
print('Третья цифра: ',c)
print('Трехзначное число - ', a,b,c, sep = '')
print('Квадрат трехзначного числа', A, 'равен', B)
