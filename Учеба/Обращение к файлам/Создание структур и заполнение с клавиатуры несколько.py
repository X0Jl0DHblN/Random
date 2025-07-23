print('Создание структур и заполнение с клавиатуры')



class Tbook:
    author = ' '
    title = '' 
    pages = 0 
    
  
N = int(input('Введите количество книг: '))

books = [Tbook() for i in range(N)]

for i in range(N):
    books[i].author = input('Введите автора: ')
    books[i].title = input('Введите название: ')
    books[i].pages = int(input('Введите количество страниц: '))

books[1].pages = books[1].pages - 10

print('-' * 35)
print(' Автор ', ' Название ', 'Кол.стр' )
print('-' * 35)
for i in range(N):
    print(books[i].author,books[i].title,books[i].pages)






