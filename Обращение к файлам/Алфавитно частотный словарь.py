print('Действия с элементами файла - Алфавитно частотный словарь')
print()

Fin = open('E:\Engl_len.txt','r')

dict_alf = {}
List = []
Sum = 0
while True:
    Str = Fin.readline() # читаем строку
    List += Str.split() # разбиваем строку на список
    if not Str:
        break
print(List)


for x in List:
    if x == dict_alf  :
        Sum += 1
print(Sum,'раз, встречается искомое слово', say)    
