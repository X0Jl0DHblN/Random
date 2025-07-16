print('Проверка простое число или не простое')
print()
N = int(input('Введите число N: '))
ost = 1
d = 2
while ost != 0:
    ost = N % d
    if ost != 0:
        d = d + 1
if d == N:
    print('Число ', N, ' простое')       
else:
    print ('Число ', N, 'не простое')