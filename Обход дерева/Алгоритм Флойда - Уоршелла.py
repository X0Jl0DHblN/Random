print('Алгоритм Флойда - Уоршелла')


N = 6
INF = 10000
select = [False] * N
dist = [INF] * N

print('Матрица смежности')
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
    
for k in range(N):
    for i in range(N):
        for j in range(N):
            if W[i][k] + W[k][j] < W[i][j]:
                W[i][j] = W[i][k] + W[k][j]

                
print('\n Матрица смежности с длинами кратчайших маршрутов между всеми вершинами \n')
for i in range(N):
    for j in range(N):
        print('{:8d}'.format(W[i][j]), end = '')
    print()