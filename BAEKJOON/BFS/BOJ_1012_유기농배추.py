import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

'''
m은 가로, n은 세로
'''

dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(a,b):

    q = deque()
    q.append((a,b))

    while q:

        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    q.append((nx,ny))


# board = []
for _ in range(t):

    m,n,k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    cnt = 0

    for _ in range(k):

        a,b = map(int, input().split())
        board[b][a] = 1


    for i in range(n):
        for j in range(m):

            if board[i][j] == 1:
                bfs(i,j)
                cnt += 1

    print(cnt)