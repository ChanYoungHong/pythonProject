import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)

'''
1. 궁금한 점 방문 했는지 확인을 해야할까 ?? 굳이 해야하나 ?
2. 
'''

n = int(input())
board = [list(input().rstrip()) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

visited = [[False] * n for _ in range(n)]

def dfs(x,y):

    visited[x][y] = True
    current_color = board[x][y]

    for i in range(4):

        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
            if current_color == board[nx][ny]:
                dfs(nx,ny)


cnt1 = 0
cnt2 = 0
res = []

for i in range(n):
    for j in range(n):

        if visited[i][j] == False:
            # board[i][j] = True
            dfs(i,j)
            cnt1 += 1

res.append(cnt1)

visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):

        if board[i][j] == 'G':
            board[i][j] = 'R'

for i in range(n):
    for j in range(n):

        if visited[i][j] == False:
            # board[i][j] = True
            dfs(i,j)
            cnt2 += 1
res.append(cnt2)

print(*res)

