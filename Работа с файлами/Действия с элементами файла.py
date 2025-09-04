print('Действия с элементами файла')

Fin = open('G:\input.txt','r')
Fout = open('G:\probaout_pr.txt','w')

List = Fin.readline().split()
print(List)
A = [int(n) for n in List]


List_1 = []

for x in List:
    x = int(x)
    List_1.append(x)
print(List_1)
#print(type(List_1[1]))

A = []
for n in List_1:
    pr = n * 2
    A.append(pr)
print(A)
      
for x in A:
    Fout.write(str(x) + ', ')