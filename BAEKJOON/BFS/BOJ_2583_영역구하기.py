import sys
from collections import deque

input = sys.stdin.readline

m,n,k = map(int, input().split())
graph = [[1] * n for _ in range(m)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):

    q = deque()
    q.append((x,y))
    cnt = 1
    while q:

        y,x = q.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[ny][nx] == 1:
                    graph[ny][nx] = 0
                    q.append((ny,nx))
                    cnt += 1

    return cnt

for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for j in range(y1, y2):
        for k in range(x1, x2):
            graph[j][k] = 0

res = []
for i in range(m):
    for j in range(n):

        if graph[i][j] == 1:
            graph[i][j] = 0
            res.append(bfs(i,j))

print(len(res))
res.sort()
for i in res:
    print(i, end=' ')
