import sys
from collections import deque


n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

cnt = 0

def bfs(x,y):

    global cnt

    q = deque()
    q.append((x,y))

    cnt = 1
    while q:

        x,y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    cnt += 1
                    q.append((nx,ny))

    return cnt

res = []
for i in range(n):
    for j in range(n):

        if board[i][j] == 1:
            board[i][j] = 0
            res.append(bfs(i,j))
            cnt = 0

print(len(res))
res.sort()

for k in res:
    print(k)



