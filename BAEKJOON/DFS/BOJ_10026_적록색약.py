import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):

    q = deque()
    q.append((x, y))

    global cnt1, cnt2
    current_color = graph[x][y]

    while q:

        x, y = q.popleft()

        for i in range(4):

            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if visited[nx][ny] == False and current_color == graph[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))


cnt1 = 0
cnt2 = 0

res = []

for i in range(n):
    for j in range(n):

        if not visited[i][j]:
            bfs(i, j)
            res.append(cnt1)
            cnt1 += 1

for i in range(n):
    for j in range(n):

        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False] * n for _ in range(n)]


for i in range(n):
    for j in range(n):

        if not visited[i][j]:
            bfs(i,j)
            res.append(cnt2)
            cnt2 += 1

print(cnt1, cnt2)
