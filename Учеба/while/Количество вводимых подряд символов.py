print()
print('---Количество вводимых подряд символов---')

count = 0

while count < 5:
    Sim = input('Введите символ: ')
    if Sim == 'f':
       count += 1
    else:
        count = 0
print('Количество введенных подряд символов f равняется:', count) 