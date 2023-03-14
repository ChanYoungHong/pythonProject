import sys
from collections import deque

input = sys.stdin.readline

m,n,k = map(int, input().split())

graph = [[1] * (n) for i in range(m)]

for _ in range(k):

    x1, y1, x2, y2 = map(int, input().split())

    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 0

print(graph)

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def bfs(x,y):

    q = deque()
    q.append((x,y))
    cnt = 1
    while q:

        y,x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    q.append((ny, nx))
                    cnt += 1

    return cnt


res = []
for i in range(m):
    for j in range(n):

        if graph[i][j] == 1:
            graph[i][j] = 0
            res.append(bfs(i,j))

print(len(res))

for i in sorted(res):
    print(i, end=' ')