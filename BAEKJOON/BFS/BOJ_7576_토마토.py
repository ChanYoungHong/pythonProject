from collections import deque
import sys

input = sys.stdin.readline

m, n = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):

        if graph[i][j] == 1:
            q.append((i, j))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():

    while q:

        x,y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0:
                    graph[nx][ny] = graph[x][y] + 1
                    q.append((nx,ny))

bfs()

res = 0
for i in graph:
    if j in i:
        if j == 0:
            print(-1)
            exit(1)

    res = max(res, max(i))

print(res - 1)
