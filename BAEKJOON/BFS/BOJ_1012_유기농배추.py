import sys
from collections import deque

'''
m - 가로
n - 세로
'''

dx = [1,-1,0,0]
dy = [0,0,-1,1]


def bfs(x,y):

    q = deque()
    q.append((x,y))

    while q:

        x,y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    q.append((nx,ny))


t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    cnt = 0

    for i in range(k):
        a, b = map(int, input().split())
        board[b][a] = 1

    for i in range(n):
        for j in range(m):

            if board[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)
    print(board)