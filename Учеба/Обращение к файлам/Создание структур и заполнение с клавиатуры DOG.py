print('Создание структур и заполнение с клавиатуры и запись в файл List_of_dogs')

import pickle

Fout = open('E:\List_of_dogs.dat','wb')

class Tbook:
    name = ' '
    breed  = '' 
    age = 0 
    
  
N = int(input('Введите количество записей: '))

List_of_dogs = [Tbook() for i in range(N)]

for i in range(N):
    List_of_dogs[i].name = input('Введите кличку: ')
    List_of_dogs[i].breed = input('Введите породу: ')
    List_of_dogs[i].age = int(input('Введите возраст: '))

List_of_dogs[1].age = List_of_dogs[1].age - 10

print('-' * 35)
print(' Автор ', ' Название ', 'Кол.стр' )
print('-' * 35)
for i in range(N):
    print(List_of_dogs[i].name,List_of_dogs[i].breed,List_of_dogs[i].age)
    
    
pickle.dump(List_of_dogs, Fout)
Fout.close()