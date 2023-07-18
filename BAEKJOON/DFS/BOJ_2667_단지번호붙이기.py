import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
board = [list(map(int, input().rstrip())) for i in range(n)]
res = []

cnt = 0

def dfs(x,y):

    global cnt

    board[x][y] = 0
    cnt += 1


    for i in range(4):
        nx = dx[i] + x
        ny = dy[i] + y

        if 0 <= nx < n and 0 <= ny < n:
            if board[nx][ny] == 1:
                dfs(nx,ny)

res = []

for i in range(n):
    for j in range(n):

        if board[i][j] == 1:
            dfs(i,j)
            res.append(cnt)
            cnt = 0

print(res)
res.sort()
for i in res:
    print(i)
