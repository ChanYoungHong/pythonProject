import sys
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

result = []
def bfs(x,y):
    home = 1
    q = deque()
    q.append((x,y))
    graph[x][y] = 0
    while q:

        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx,ny))
                    home += 1

    result.append(home)

cnt = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)
            cnt += 1

result.sort()

print(cnt)
for i in result:
    print(i)