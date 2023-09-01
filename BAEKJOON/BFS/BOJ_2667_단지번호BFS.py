import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def bfs(x,y):

    global cnt

    q = deque()
    q.append((x,y))
    cnt = 1

    while q:

        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    q.append((nx,ny))
                    cnt += 1


    return cnt


cnt = 0
res = []
for i in range(n):
    for j in range(n):

        if board[i][j] == 1:
            board[i][j] = 0
            res.append(bfs(i,j))
            cnt = 0

print(len(res))
res.sort()
for i in res:
    print(i)