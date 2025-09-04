print('Алгоритм обхода дерева')

class TNode:
    pass


def node(d, L = None, R = None):
    newNode = TNode()
    newNode.data = d
    newNode.left = L
    newNode.right = R
    return newNode

T = node('*', node('+', node('1'), node('4')),
         node('-', node('9'), node('5'))
         )

# =============================================================================
# def DFS(T):
#     if not T:
#         return
#     else:print(T.data, end = '')
#     DFS(T.left)
#     DFS(T.right)
#     
# DFS(T)
# =============================================================================

    
# =============================================================================
# def DFS_stack(T):
#     stack = [T]
#     while stack:
#         v = stack.pop()
#         print(v.data, end = '')
#         if v.right:
#             stack.append(v.right)
#         if v.left:
#             stack.append(v.left)
#             
# DFS_stack(T)            
#             
# =============================================================================
            
def BFS(T):
    quene = [T]
    while quene:
        v = quene.pop()
        print(v.data, end = '')
        if v.left:
            quene.append(v.left)
        if v.right:
            quene.append(v.right)
                
BFS(T)            
