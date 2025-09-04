print('Действия с элементами файла - сортировка')
print()
Fin = open('G:\Sort.txt','r')
Fout = open('G:\Sortout.txt','w')

List = []
while True:
    Str = Fin.readline() # читаем строку
    List += Str.split() # разбиваем строку на список
    if not Str:
        break

List_1 = []
for x in List:
    x = int(x)
    List_1.append(x)
print(List_1)

for i in range(len(List_1)):
    index_Min = i
    for j in range(i + 1,len(List_1)):
        if List_1[j] < List_1[index_Min]:
            index_Min = j
    if index_Min != i:
       List_1[i],List_1[index_Min] = List_1[index_Min],List_1[i]
print()
print('Отсортированный список:')
print()
print(List_1)


for x in List_1:
    Fout.write(str(x) + ', ')
