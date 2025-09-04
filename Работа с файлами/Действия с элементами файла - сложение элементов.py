print('Действия с элементами файла - сложение элементов')
print()
Fin = open('G:\File_in.txt','r')
Fout = open('G:\File_sum.txt','w')



 
while True:
    Str = Fin.readline()
    List = Str.split()
    print(Str)
    print(List)
    a,b = [int(x) for x in List]
    #x = List[0]
    #y = List[1]
    #print(x,y)
    #x = int(List[0])
    #y = int(List[1])
    #z = x + y
    #print(x,y,z)
    if not Str:
        break



