
print('Функция filtr() и применение ЛФ в фильтре')


numbers = [1, 2, 3, 4, 5, 7, 8, 10, 11]
print('Исходный список: ', numbers)

# =============================================================================
# def filt(n):
#     if n % 2 == 0:
#         return True
#     else:
#         False
# 
# new_numbers = filter(filt,numbers)
# print('Отфильтрованный список: ', list(new_numbers))        
# =============================================================================

new_numbers = list(filter(lambda x: (x % 2 == 0),numbers))
print('Отфильтрованный список: ', new_numbers)                
                   