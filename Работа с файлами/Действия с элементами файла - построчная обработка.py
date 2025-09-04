print('Действия с элементами файла - построчная обработка')
print()
Fin = open('G:\DOG.txt','r')
Fout = open('G:\DOG_select.txt','w')


   
while True:
    Str = Fin.readline() 
    if not Str:
        break
    age = int(Str.split(';')[1])
    if age < 5:
        Fout.write(Str)      
        
        
        
        
        
        