print('Steck') 


#Fout = open('E:\test_steck.txt','w')
Fin = open('E:\input.txt','r')

Y = []
steck = []


while True:
    Str = Fin.readline() # читаем строку
    Y += Str.split() # разбиваем строку на список
    if not Str:
        break

for x in Y:
    x = int(x)
    steck.append(x)
print(steck)





   
   