print('Действия с элементами файла - поиск Мах и Min значения') 
from random import*

Fout = open('G:\File_rand_el.txt','w')
Fin = open('G:\File_rand_el.txt','r')


A = [randint(-100,100) for i in range(50)]
print(A)  

Fout.write(str(A))

#Нужно прочитать файл и далее работать с полученными значениями






        
        







