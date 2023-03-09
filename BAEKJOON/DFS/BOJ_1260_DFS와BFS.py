import sys
from collections import deque

input = sys.stdin.readline

n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]

visited = [False] * (n + 1)
visited2 = [False] * (n + 1)

# for i in range(m):
#     a, b = map(int, input().split())
#     graph1[a].append(b)
#     graph1[b].append(a)
# print(graph1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True


res = []


def bfs(v):
    q = deque([v])
    visited[v] = True
    while q:
        pop = q.popleft()
        print(pop, end=' ')
        # for i in graph[pop]:
        for i in range(1, n+1):
            if visited[i] == False and graph[pop][i]:
                visited[i] = True
                q.append(i)
            # if pop not in res:
            #     res.append(pop)


def dfs(v):
    visited2[v] = True
    print(v, end=' ')
    for i in range(1, n + 1):
        if visited2[i] == False and graph[v][i]:
            dfs(i)


dfs(v)
print()
bfs(v)
