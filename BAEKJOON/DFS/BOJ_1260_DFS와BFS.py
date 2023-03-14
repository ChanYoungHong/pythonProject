import sys
from collections import deque

input = sys.stdin.readline

n,m,k = map(int, input().split())

graph = [[0] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())

    # graph[a].append(b)
    # graph[b].append(a)
    graph[a][b] = True
    graph[b][a] = True


visited1 = [False] * (n+1)
visited2 = [False] * (n+1)

def bfs(k):

    q = deque([k])
    visited2[k] = True
    while q:
        t = q.popleft()
        print(t, end=' ')
        for i in range(1, n+1):
            if visited2[i] == False and graph[t][i]:
                visited2[i] = True
                q.append(i)



def dfs(k):
    visited1[k] = True
    print(k, end=' ')

    for i in range(1, n+1):
        if visited1[i] == False and graph[k][i]:
            dfs(i)



dfs(k)
print()
bfs(k)
