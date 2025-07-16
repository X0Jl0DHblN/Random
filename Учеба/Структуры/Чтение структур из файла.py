print('Чтение структур из файла')

import pickle

Fin = open('G:\List_books','rb')

class Tbook:
    author = ' '
    title = '' 
    pages = 0

# =============================================================================
# N = 1
# a = pickle.load(Fin)
# for i in range(N):
#     print(a[i].name,a[i].breed,a[i].age)
# Fin.close()
# =============================================================================

a = pickle.load(Fin)
print(a.author, a.title, a.pages)
Fin.close


