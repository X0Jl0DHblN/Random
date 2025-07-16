print('Задача - магазин')

def printline():
    return print('=================')
printline()


Set = {'огурец': 10, 'тыква': 2, 'морковь': 12, 'картошка': 9, 'укроп': 25, 'помидоры': 19, 'варенье': 34}
List_keys = list(Set.keys())
Product = ('Продукт')
Price = ('Цена')
print('{: >8} {: >7}'.format(Product,Price))
printline()

for x in Set:
    print('{: <8} {:>2} {: >3}'.format(x,':', Set[x]))
prod_name = input('Введите название товара: ')
quantity = int(input('Введите количество: '))

printline()
print()
Set_price = Set.get(prod_name)
prod_price = quantity * Set_price
print('Общая стоимость покупки составляет - {} руб.'.format(prod_price))






