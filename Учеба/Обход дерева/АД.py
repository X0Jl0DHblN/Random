print('Алгоритм Дейкстры')



N = 6
INF = 10000
select = [False] * N
dist = [INF] * N



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

start = 0
V = start
dist[start] = 0

minDist = 0

while minDist < INF:
    select[V] = True
    for j in range(N):
        if dist[V] + W[V][j] < dist[j]:
            dist[j] = dist[V] + W[V][j]
            

    minDist = INF
    for j in range(N):
        if not select[j] and dist[j] < minDist:
            minDist = dist[j]
            V = j
            
print(select)
print(dist)
