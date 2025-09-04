print('Удаление пробелов в начале строки')# доделать

S = input('Введите строку: ')

#print(S.lstrip())


print()
#print('Метод 2')

S_New = '1'
ch = ''
while S[0:] == ' ' and len(S) != 1:  #
    S[0:] = ch
    S_New = S_New + S
print(S_New)
