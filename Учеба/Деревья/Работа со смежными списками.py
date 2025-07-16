print('Работа со смежными списками')

def CountPath(G, vStart, vEnd, visit):
    if vStart == vEnd:
        return 1
    visit.append(vStart)
    count = 0
    for V in G[vStart]:
        if not V in visit:
            count = count + CountPath(G, V, vEnd, visit)
    visit.pop()
    return count
# =============================================================================
# G = [[3],
#      [0,2],
#      [],
#      [1,2,4],
#      [2]]
# 
# =============================================================================

G = [[1,2,3], #0-А
     [6,3], #1-Б
     [3,7,8], # 2-В
     [7,5], # 3-Г
     [5,9], # 4-Д
     [7,8,9], # 5-У
     [3,4,9], # 6-Ж
     [8], # 7-И
     [9], # 8-К
     [10,11,12], # 9-Л
     [12], # 10-M
     [12], # 11-H
     [12]] # 12-П

Start = int(input('Введите начальную вершину: ')) 
Fin = int(input('Введите конечную вершину: '))
I_Point = int(input('Введите промежуточную вершину: '))


count_1 = (CountPath(G,Start,I_Point,[]))
count_2 = (CountPath(G,I_Point,Fin,[]))
print('Количество путей в промежуточную точку - ',count_1)
print('Количество путей из промежуточную точки в конечную - ',count_2)

Quant_road = count_1 + count_2
print()
print('Количество путей из вершины - {}, в вершину - {}, равняется - {} '.format(Start, Fin, Quant_road))