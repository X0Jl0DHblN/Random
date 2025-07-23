print('Создание, запись и чтение с последующей сортировкой структуры')

import pickle


Fout = open('E:\List_books.dat','wb')


class Tbook:
    name = ' '
    breed  = '' 
    age = 0 
    
  
N = int(input('Введите количество записей: '))

books = [Tbook() for i in range(N)]

for i in range(N):
    books[i].name = input('Фамилия автора: ')
    books[i].breed = input('Название произведения: ')
    books[i].age = int(input('Количество страниц: '))


print('-' * 35)
print(' Автор ', ' Название ', 'Кол.стр' )
print('-' * 35)
for i in range(N):
    print(books[i].name,books[i].breed,books[i].age)
    
pickle.dump(books, Fout)
Fout.close()



# =============================================================================
# Fin = open('E:\List_books.dat','rb')
# 
# books = [0] * N
# 
# for i in range(N):
#     books = pickle.load(Fin)
# 
# print(books)
# =============================================================================


# =============================================================================
# n = len(books) 
# for i in range(n-1):
#     for j in range(n-2, i-1, -1):
#         if books[j].name > books[j+1].name:
#             books[j],books[j+1] = books[j+1],books[j]        
# 
# print()
# print('Отсортированный список авторов')    
# print('-' * 35)
# print(' Автор ', ' Название ', 'Кол.стр' )
# print('-' * 35)
# for i in range(N):
#     print(books[i].name,books[i].breed,books[i].age)    
# =============================================================================
