print('Создание структур и заполнение с клавиатуры и запись в файл')

import pickle

Fout = open('G:\Struct_29_03.dat','wb')

class Tbook:
    author = ' '
    title = '' 
    pages = 0 

b = Tbook()

b.author = input('Введите автора: ')
b.title = input('Введите название: ')
b.pages = int(input('Введите количество страниц: '))

print('-' * 35)
print(' Автор ', ' Название ', 'Кол.стр' )
print('-' * 35)
print(b.author, b.title, b.pages)

pickle.dump(b, Fout)
Fout.close()
