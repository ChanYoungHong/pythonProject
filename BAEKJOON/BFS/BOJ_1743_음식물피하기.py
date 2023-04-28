import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

n,m, cn = map(int, input().split())

graph = [[0] * m for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y):

    global cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if graph[nx][ny] == '#':
                graph[nx][ny] = 0
                dfs(nx,ny)
                cnt += 1


for i in range(cn):

    a,b = map(int, input().split())
    graph[a-1][b-1] = '#'

res = 0
cnt = 0
for i in range(n):
    for j in range(m):

        if graph[i][j] == '#':
            cnt = 0
            dfs(i,j)
            res = max(res, cnt)

print(res)









