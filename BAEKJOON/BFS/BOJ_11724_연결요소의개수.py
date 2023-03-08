import sys
from collections import deque


input = sys.stdin.readline

n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)
cnt = 0
def bfs(v):

    global cnt
    q = deque(graph[v])
    print('qqqqq', q)
    while q:
        pop = q.popleft()
        print('poppp = ', pop)
        for i in graph[pop]:
            print(visited)
            if visited[i] == False:
                visited[i] = True
                print(i)
                q.append(i)
                print(q)

for i in range(1, n+1):
    if not visited[i]:
        ''' 이 조건 이 이해가 잘 안 됨 not graph[i] 의미... ?! '''
        if graph[i] == False:
            cnt += 1
            visited[i] = True
        else:
            bfs(i)
            print(i)
            cnt += 1
