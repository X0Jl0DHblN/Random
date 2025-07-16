print('Обращение к файлу, создать список из строк прочитанного файла')

Fin = open('G:\Engl_len.txt','r')

List = []
while True:
    Str = Fin.readlines() # читаем файл
    List += Str
    if not Str:
        break
print(List)
print()
print('Список состоит из {} строк'.format(len(List)))



  