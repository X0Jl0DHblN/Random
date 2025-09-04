print('Обращение к файлу readline')

Fin = open('G:\input.txt','r')
List = []
while True:
    Str = Fin.readline()
    #print(Str)
    #Str = Fin.readline().split()
    List += Str.split()
    print(List)
    if not Str:
        break
    
#print(List, end = '')
