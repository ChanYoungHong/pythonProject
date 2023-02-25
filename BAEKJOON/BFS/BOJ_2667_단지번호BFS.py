import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


res = []

def bfs(x,y):

    cnt = 1
    q = deque()
    q.append((x,y))

    while q:

        x,y = q.popleft()
        graph[x][y] = 0

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    q.append((nx,ny))
                    cnt += 1

    res.append(cnt)

house = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            bfs(i,j)
            house += 1

print(house)
res.sort()

for i in res:
    print(i)
