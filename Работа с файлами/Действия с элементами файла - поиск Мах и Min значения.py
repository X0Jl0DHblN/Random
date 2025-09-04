print('Действия с элементами файла - найти Max и Min значение положительных чисел элементов файла')
print()
 
Fin = open('G:\File_rand_el.txt','r')
Fout = open('G:\File_Max_Min_el_1.txt','w')
 
List = []
while True:
    Str = Fin.readline() # читаем строку
    List += Str.split() # разбиваем строку на список
    if not Str:
        break  
List_1 = []
for x in List:
    x = int(x)
    if x > 0 and x % 2 == 0:
        List_1.append(x)
print(List_1)
 
Max = List_1[0] 
for x in List_1: 
    if x > Max:
        Max = x 
           
Min = List_1[0] 
for y in List_1: 
    if y <  Min:
        Min = y
print('Максимальное значение = ', Max)
print('Минимальное значение = ', Min)
 
res = ('Максимальное значение = {}, Минимальное значение = {}'.format(Max,Min))
 
Fout.write(str(res))
        







