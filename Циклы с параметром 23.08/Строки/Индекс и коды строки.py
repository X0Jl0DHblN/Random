print('Индекс и коды строки')

s = input('Введите строку: ')

n = len(s)
for i in range(n):
    print(s[i],' - ', ord(s[i]))
    
for ch in s:
    print(ch,' - ', ord(ch))   
    
