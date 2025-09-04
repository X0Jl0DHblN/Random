print('Нахождение минимального оставного дерева')


N = 6
INF = 1000

W = [[0,2,4,INF,INF,INF],
     [2,0,9,7,INF,INF],
     [4,9,0,8,1,INF],
     [INF,7,8,0,3,1],
     [INF,INF,1,3,0,2,],
     [INF,INF,INF,1,2,0]]

print()
for i in range(N):
    for j in range(N):
        print('{:8d}'.format(W[i][j]), end = '')
    print()

col = [i for i in range(N)]
print(col)


ostov = []

for k in range(N-1): 
    min_Dist = 10e10 
    for i in range(N):
        for j in range(N):
            if col[i] != col[j] and W[i][j] < min_Dist:
                i_min = i
                j_min = j
                min_Dist = W[i][j]
    ostov.append((i_min, j_min)) 
    c = col[j_min]
    for i in range(N):
        if col[i] == c:
            col[i] = col[i_min]
        
for edge in ostov:
    print('(', edge[0],',',edge[1],')')       




# =============================================================================
# W = [[0] * N for i in range(N)]
# 
# for i in range(N):
#     for j in range(N):
#         W[i][j] = int(input('Введите элемент: '))
# print(W)    
#   
# 
# =============================================================================
