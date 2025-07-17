print('Замена символов в строке без использования метода')

s = input('Введите строку: ')
print(s)

n = len(s)
new_s = ''

for i in range(n):
    if s[i] == '.':
        sym = '0'
    else:    
        if s[i] == 'x' or s[i] == 'X':
            sym = '1'
        else:    
            sym = s[i]
    new_s = new_s + sym
    
print(new_s)        