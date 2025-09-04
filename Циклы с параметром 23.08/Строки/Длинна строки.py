

print('Длинна строки')

Line = input('Введите строку из стихотворения: ')
Lin_len = len(Line)
print('Длинна введенной строки составляет',Lin_len, 'символа')
print()


print('Метод 2')
count = 0
for i in Line:
    count += 1
print('Длинна введенной строки составляет',count, 'символа')  

print('Метод 3')
 