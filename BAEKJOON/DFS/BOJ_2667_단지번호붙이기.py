import sys

input = sys.stdin.readline

n = int(input())

dx = [-1,1,0,0]
dy = [0,0,1,-1]

visited = [[False] * n for _ in range(n)]
graph = [list(map(int, input().rstrip())) for _ in range(n)]

cnt = 0
def dfs(x,y):

    global cnt
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and graph[nx][ny] == 1:
                dfs(nx,ny)
                cnt += 1

    return cnt

res = []
house = 0
for i in range(n):
    for j in range(n):

        if visited[i][j] == False and graph[i][j] == 1:
            cnt = 1
            dfs(i,j)
            res.append(cnt)

print(len(res))
for i in sorted(res):
    print(i)