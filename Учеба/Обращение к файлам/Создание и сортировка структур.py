print('Создание и сортировка структур')


class Tbook:
    name = ' '
    breed  = '' 
    age = 0 
    
  
N = int(input('Введите количество записей: '))

List_of_authors = [Tbook() for i in range(N)]

for i in range(N):
    List_of_authors[i].name = input('Фамилия автора: ')
    List_of_authors[i].breed = input('Название произведения: ')
    List_of_authors[i].age = int(input('Количество страниц: '))


print('-' * 35)
print(' Автор ', ' Название ', 'Кол.стр' )
print('-' * 35)
for i in range(N):
    print(List_of_authors[i].name,List_of_authors[i].breed,List_of_authors[i].age)


n = len(List_of_authors) 
for i in range(n-1):
    for j in range(n-2, i-1, -1):
        if List_of_authors[j].name > List_of_authors[j+1].name:
            List_of_authors[j],List_of_authors[j+1] = List_of_authors[j+1],List_of_authors[j]        

print()
print('Отсортированный список авторов')    
print('-' * 35)
print(' Автор ', ' Название ', 'Кол.стр' )
print('-' * 35)
for i in range(N):
    print(List_of_authors[i].name,List_of_authors[i].breed,List_of_authors[i].age)    


