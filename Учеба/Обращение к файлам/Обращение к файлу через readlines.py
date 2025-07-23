print('Обращение к файлу через readlines')# Доделать

Fin = open('G:\input.txt','r')

List = Fin.readlines()
print(List)
Fin.close()
for s in List:
    print(s)