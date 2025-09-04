
print('Применение ЛФ в функции map()')

old_list = [1, 2, 3, 4, 5]
print('Старый список: ', old_list)
new_list = list(map(lambda x: x * 2, old_list))
print('Новый список: ', new_list)

