import sys
from collections import deque

input = sys.stdin.readline


n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

cnt = 0

def bfs(x,y):

    global cnt
    cnt = 1

    q = deque()
    q.append((x,y))

    while q:

        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

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



res.sort()
print(len(res))
for i in res:
    print(i)

