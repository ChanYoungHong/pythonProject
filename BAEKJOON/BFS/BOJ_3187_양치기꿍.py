import sys
from collections import deque

input = sys.stdin.readline



dx = [-1,1,0,0]
dy = [0,0,-1,1]

wolf = 0
sheep = 0

def bfs(x,y):

    global wolf, sheep

    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    while q:

        x,y = q.popleft()

        if graph[x][y] == 'v':
            wolf += 1

        if graph[x][y] == 'k':
            sheep += 1

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] != '#' and visited[nx][ny] == False:
                    visited[nx][ny] = 1
                    q.append((nx,ny))


n, m = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

tem1 = 0
tem2 = 0

for i in range(n):
    for j in range(m):

        if graph[i][j] != '#' and visited[i][j] == False:
            bfs(i,j)

            if wolf >= sheep:
                sheep = 0
            else:
                wolf = 0

            tem1 += sheep
            tem2 += wolf

            sheep = 0
            wolf = 0

bfs(0,0)
print(tem1, tem2)