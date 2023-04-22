import sys
from collections import deque

input = sys.stdin.readline






n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# board = [list(map(int, input()))]

dx = [-1,1,0,0]
dy = [0,0,-1,1]



def dfs(x,y):

    global cnt
    visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if visited[nx][ny] == False and board[nx][ny] == 1:
                dfs(nx,ny)
                cnt += 1


cnt = 0
res = []
for i in range(n):
    for j in range(n):

        if board[i][j] == 1 and visited[i][j] == False:
            cnt = 1
            dfs(i,j)
            res.append(cnt)


print(len(res))
for i in res:
    print(i)