
import sys

input = sys.stdin.readline

n = int(input())

graph = [list(map(str, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

three_cnt, two_cnt = 0, 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):

    visited[x][y] = True
    current_color = graph[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= n:
            continue

        if visited[nx][ny] == False:
            if graph[nx][ny] == current_color:
                dfs(nx,ny)


for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            three_cnt += 1


for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            two_cnt += 1

print(three_cnt, two_cnt)