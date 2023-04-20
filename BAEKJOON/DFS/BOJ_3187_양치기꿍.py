import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):

    global wolf, sheep
    visited[x][y] = True

    if board[x][y] == 'v':
        wolf += 1

    if board[x][y] == 'k':
        sheep += 1

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] != '#':
            dfs(nx,ny)



wolf = 0
sheep = 0

tem1 = 0
tem2 = 0

for i in range(n):
    for j in range(m):

        if board[i][j] != '#' and not visited[i][j]:

            wolf = 0
            sheep = 0


            dfs(i,j)
            visited[i][j] = True

            if wolf >= sheep:
                sheep = 0
            else:
                wolf = 0

            tem1 += wolf
            tem2 += sheep

print(tem2, tem1)

