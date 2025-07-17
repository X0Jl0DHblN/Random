print('Steck рабочий') 

stack = []

for s in open('E:\input.txt','r'):
    stack.append(int(s))
    
print(stack)

Fout = open('E:\stack_1.txt','w')

while len(stack) > 0:
    x = stack.pop()
    Fout.write(str(x) + '\n')
Fout.close()    

