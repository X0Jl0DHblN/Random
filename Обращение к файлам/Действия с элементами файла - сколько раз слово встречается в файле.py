print('Действия с элементами файла - сколько раз слово встречается в файле')
print()

Fin = open('E:\Engl_len.txt','r')


List = []
say = input('Введите искомое слово:')
Sum = 0
while True:
    Str = Fin.readline() # читаем строку
    List += Str.split() # разбиваем строку на список
    if not Str:
        break
print()

for x in List:
    if x == say:
        Sum += 1
print(Sum,'раз, встречается искомое слово', say)    
   
