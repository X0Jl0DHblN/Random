print('Обращение к файлу append')

Fin = open('G:\input.txt','r')
Fout = open('G:\probaout.txt','w')
Fout_1 = open('G:\probaout_1.txt','w')
 
Fin = open('G:\input.txt','r')
List = []
while True:
    Str = Fin.readline() # читаем строку
    Fout_1.write(Str) # запись в новый файл прочитанной строки
    List += Str.split() # разбиваем строку на список
    if not Str:
        break
print(List)

List_1 = []
for x in List:
    x = int(x)
    List_1.append(x)
    print(List_1)
    
for x in List_1:
    Fout.write(str(x) + ', ')
    
    
