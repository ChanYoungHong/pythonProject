import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

noSick, getSick = 0, 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def dfs(x, y):

    visited[x][y] = True
    current_color = graph[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if (0 <= nx < n) and (0 <= ny < n):
            if visited[nx][ny] == False:
                if graph[nx][ny] == current_color:
                    dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            noSick += 1

for i in range(n):
    for j in range(n):
        if graph[i][j] == 'G':
            graph[i][j] = 'R'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i, j)
            getSick += 1

print(noSick, getSick)
