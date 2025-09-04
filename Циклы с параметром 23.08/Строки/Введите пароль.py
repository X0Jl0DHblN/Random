import sys  

s = input('Введите пароль: ')

password = '159#'

if s == password:
    print('Пожалуйста войдите')
else:
    print('Пароль введен неправильно')
    sys.exit() 