print('Обращение к файлу readline')

Fin = open('G:\input.txt','r')
List = []
while True:
    Str = Fin.readline().split()
    List += list(Str)
    if not Str:
        break
    
print(List, end = '')




spisok = []
 
for i in Fin:
    spisok.append(i.rstrip())
 
print(spisok)