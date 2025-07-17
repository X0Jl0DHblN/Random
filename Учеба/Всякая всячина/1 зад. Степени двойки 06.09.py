print()
print('Количество степеней двойки')
print()
N = int(input('Введите количество степеней двойки: '))
print(' Степень  ', '|','   Значение')
for i in range(N):
    x = 2 ** i
    print('{:4} {:16}'.format(i,x))