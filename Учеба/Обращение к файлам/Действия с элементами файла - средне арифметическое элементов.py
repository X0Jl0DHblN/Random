print('Действия с элементами файла - средне арифметическое элементов')
print()
Fin = open('G:\File_in_el.txt','r')
Fout = open('G:\File_sr_el.txt','w')

List = []
while True:
    Str = Fin.readline() # читаем строку
    List += Str.split() # разбиваем строку на список
    if not Str:
        break
print(List)    
Sum = 0
for x in List:
    x = int(x)
    Sum += x
Sr_el = Sum / len(List)  
  
print(Sr_el)


Fout.write(str(Sr_el))