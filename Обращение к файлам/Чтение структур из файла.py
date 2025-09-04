print('Чтение структур из файла')

import pickle

Fin = open('E:\List_books.dat','rb')

Book = [0] * 3

for i in range(3):
    Book = pickle.load(Fin)

print(Book)

