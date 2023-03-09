import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
link = int(input())

graph = [[] for i in range(n+1)]
visited = [False] * (n+1)

for i in range(link):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
def bfs(graph, v):

    global cnt
    q = deque(graph[v])
    print('qqq', q)
    while q:

        pop = q.popleft()
        visited[pop] = True

        for i in graph[pop]:
            if visited[i] == False:
                visited[i] = True
                q.append(i)
                cnt += 1

    print(cnt)


bfs(graph, 1)
