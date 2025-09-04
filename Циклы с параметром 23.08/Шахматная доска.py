print('Шахматная доска')

N = int(input('Введите количество клеточек: '))
A = int(input('Введите высоту шахматной доски: '))
Sim = input('Введите символ: ')
print()

for i in range(A - 3): 
# Основной блок   
    print('    ', end = '')
    for i in range(N):
        i = Sim
        print('{:4}'.format(i), end = '')
    print()
    for i in range(N):
        i = Sim
        print('  ''{:2}'.format(i), end = '')
    print()

# 2-й блок

