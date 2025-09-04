import sys

print('Операция конкотенация')

S = input('Введите строку: ')
S_New = ''

for ch in S:
    if ch == 'е':
        ch = 'и'        
    S_New = S_New + ch 
    sys.exit() 
print(S_New)





