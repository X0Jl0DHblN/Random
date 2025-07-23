print('Процентная чтавка по вкладу')

Summa_v = int(input('Введите сумму вклада: '))
Srok_v = int(input('Введите срок вклада (дней): '))
Proc_v = int(input('Введите процентную ставку (годовых): '))

def max_meaning (a,b):
    if a > b:
        return print('>')
    elif a == b:
        return print('<')
    else:
        return print('=')
          
max_meaning(X,Y)
