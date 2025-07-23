print('Проверка правильности расстановки скобок в строке с использованием Stack')

#S = input('Введите строку со скобками: ')
S = '(4+5)*{[10-2] / (3-4)}'

stack = [ ]

a = True

dict = {'(':')', '[':']', '{':'}'}

for ch in S:
    if ch in '([{':
        stack.append(dict[ch])
    elif ch in ')]}':
        if len(stack) == 0 or ch != stack.pop():
            a = False
            break
#if stack:
    #a = False
            
if a == True:
    print('Скобки расставлены правильно')
else:
    print('Скобки расставлены не правильно')            