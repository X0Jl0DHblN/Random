print('Стековый калькулятор')

data = input().split()

stack = [ ]
for x in data:
    if x in '+-*/':
        op2 = int(stack.pop())
        op1 = int(stack.pop())
        if x == '+': 
            res = op1 + op2
        elif x == '-':
            res = op1 - op2
        elif x == '*':
            res = op1 * op2
        else:
            res = op1 / op2
        stack.append(res)
    else:
        stack.append(x)
print(stack[0])
    