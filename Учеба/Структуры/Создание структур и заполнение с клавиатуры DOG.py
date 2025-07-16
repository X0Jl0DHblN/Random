print('Создание структур и заполнение с клавиатуры и запись в файл List_of_dogs')

import pickle

Fout = open('G:\List_of_dogs.dat','wb')

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


print('-' * 35)
print('Кличка ', '   Порода   ', ' Возраст' )
print('-' * 35)
for i in range(N):
    print('{: <8} {:>10} {: >6}'.format(List_of_dogs[i].name,List_of_dogs[i].breed,List_of_dogs[i].age))
    
    
pickle.dump(List_of_dogs, Fout)
Fout.close()
