import sys
from collections import deque

'''
1. 공기가 퍼져나가는 것을 생각하기
2. 

'''

dx = [1,-1,0,0]
dy = [0,0,1,-1]


def air_bfs(x,y):

    q = deque()
    q.append((x,y))

    while q:

        x,y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if visited[nx][ny] == 0 and board[nx][ny] == 0:
                    q.append((nx,ny))
                    visited[nx][ny] = 1

                elif board[nx][ny] == 1:
                    visited[nx][ny] = visited[nx][ny] + 1


n,m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]



time = 0
while True:


    visited = [[0] * m for _ in range(n)]
    air_bfs(0,0)
    # visited[0][0] = 1
    time += 1

    for i in range(n):
        for j in range(m):

            if visited[i][j] >= 2:
                board[i][j] = 0

    block_cnt = 0
    for i in range(n):
        for j in range(m):

            if board[i][j] == 0:
                block_cnt += 1

    if block_cnt == (n*m):
        break

print(time)
