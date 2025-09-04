print('Выделение имени файла из адреса файла')

s = input('Введите полный адрес файла') #D:/User/Users/Proba/proba.txt

def F(S):
    pos = s.rfind('/')
    name = s[pos +1:]
    return name

Name_F = F(s)

print('Имя файла -',Name_F)

