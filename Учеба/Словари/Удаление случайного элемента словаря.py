print('Удаление случайного элемента словаря')

from random import*

    
A = {1: 'a', 2: 'b', ('a','b'): 'c', 4: 'd', 5: 'e'}
print(A)
print(A.keys())
List_keys = list(A.keys())
print(List_keys)


# =============================================================================
# List_len = len(List_keys)
# print(List_len)
# number = randint(0,List_len - 1)
# print(number)
# del A[List_keys[number]] 
# print(A)
# 
# =============================================================================

key = choice(List_keys)
print(key)
del A[key]
print(A)

