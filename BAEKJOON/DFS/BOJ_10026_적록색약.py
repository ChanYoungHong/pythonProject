import sys
sys.setrecursionlimit(10000)

input = sys.stdin.readline

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

visited = [[False] * n for _ in range(n)]

def dfs(x,y):

    cur_color = board[x][y]

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if cur_color == board[nx][ny] and not visited[nx][ny]:
                visited[nx][ny] = True
                dfs(nx,ny)

cnt1 = 0
for i in range(n):
    for j in range(n):

        if visited[i][j] == False:
            dfs(i,j)
            cnt1 += 1

print(cnt1)

for i in range(n):
    for j in range(n):

        if board[i][j] == 'G':
            board[i][j] = 'R'

visited = [[False] * n for _ in range(n)]

cnt2 = 0
for i in range(n):
    for j in range(n):

        if visited[i][j] == False:
            dfs(i,j)
            cnt2 += 1

print(cnt2)
