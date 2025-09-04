print('Пифагорова таблица')
print('    ', end = '')
for i in range(1,10):
    print('{:4}'.format(i), end = '')
print()
for i in range(1,11):
    print('{:4}'.format(i), end = '')
    for j in range(1,10):
        print('{:4}'.format(i * j), end = '')
    print()    