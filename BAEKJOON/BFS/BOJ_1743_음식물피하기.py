import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def dfs(x,y):

    global cnt

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == '#':
                board[nx][ny] = 0
                dfs(nx,ny)
                cnt += 1


res = []
n,m,k = map(int, input().split())
cnt = 0
board = [[0] * (m)for _ in range(n)]
for _ in range(k):
    a,b = map(int, input().split())
    board[a-1][b-1] = '#'

for i in range(n):
    for j in range(m):
        if board[i][j] == '#':
            cnt = 0
            dfs(i,j)
            res.append(cnt)

print(max(res))



