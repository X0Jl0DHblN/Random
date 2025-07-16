print('Вычисление арифметического выражения с помощью дерева')

class TNode:
    pass

def node(d, L = None, R = None):
    newNode = TNode()
    newNode.data = d
    newNode.left = L
    newNode.right = R
    return newNode


expr = "40-2*6-4*5"
    
def priority(op):
    if op in '+-':
        return 1
    if op in '*/':
        return 2
    return 100

def lastOp(expr):
    minPrt = 50
    pos = -1
    for i in range(len(expr)):
        prt = priority(expr[i])
        if prt <= minPrt:
            minPrt = prt
            pos = i
    return pos
    
def makeTree(expr):
    pos = lastOp(expr)
    if pos < 0:
        Tree = node(expr)
    else:
        Tree = node(expr[pos])
        Tree.left = makeTree(expr[:pos])
        Tree.right = makeTree(expr[pos + 1:])
    return Tree
   
def calcTree(Tree):
    if not Tree.left:
        return int(Tree.data)
    else:
        n1 = calcTree(Tree.left)
        n2 = calcTree(Tree.right)
        return doOperation(Tree.data, n1, n2)
    
def doOperation(op, n1, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    else:
        return n1 // n2    
    
T = makeTree(expr)

print('Результат:',calcTree(T))