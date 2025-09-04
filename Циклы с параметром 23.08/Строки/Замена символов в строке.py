print('Замена символов в строке')

s = input('Введите строку: ')
print(s)

res = s.replace('.','0')
res_1 = res.replace('x','1')
res_2 = res_1.replace('X','1')
print(res_2)


