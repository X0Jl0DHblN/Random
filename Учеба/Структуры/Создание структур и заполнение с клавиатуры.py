print('Создание структур и заполнение с клавиатуры')


#N = int(input('Введите количество книг: '))
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



