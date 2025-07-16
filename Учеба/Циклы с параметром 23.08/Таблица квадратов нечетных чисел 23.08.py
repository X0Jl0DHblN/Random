print('Вычисление стоимости продуктов')
print()
Price = float(input('Введите цену одного килограмма и нажмите <Enter>: '))
print('копейки от рублей отделяйте точкой')

print('Вес', '   Стоимость')
print('(гр.)', '  (руб.)')

price_100 = Price / 10

for i in range(1,11):
     print('{:4}   {:8.2f}'.format(i * 100, price_100 * i))
