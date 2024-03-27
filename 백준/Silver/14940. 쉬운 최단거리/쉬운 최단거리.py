# import sys
# from collections import deque
#
# input = sys.stdin.readline
#
# n,m = map(int, input().split())
#
# board = [list(map(int, input().split())) for _ in range(n)]
#
#
# dx = [-1,1,0,0]
# dy = [0,0,1,-1]
#
#
#
# def bfs(start_x, start_y):
#     q = deque()
#     q.append((start_x, start_y))
#     # 시작 지점의 거리는 0으로 설정
#     board[start_x][start_y] = 0
#
#
#     while q:
#
#         x,y = q.popleft()
#         board[0][0] = 0
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < m:
#
#                 if board[nx][ny] == 1:
#                     board[nx][ny] = 0
#                     board[nx][ny] = board[x][y] + 1
#                     q.append((nx,ny))
#
# bfs(0,0)
#
# for i in board:
#     print(*i)


import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

board = [list(map(int, input().rstrip().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[-1] * m for _ in range(n)]

def bfs(a,b):
    q = deque()

    # 시작점을 큐에 추가하고 방문 표시 및 거리 초기화
    q.append((a,b))
    visited[a][b] = 0

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m and visited[nx][ny] == -1:
                if board[nx][ny] == 0:
                    visited[nx][ny] = 0
                elif board[nx][ny] == 1:
                    visited[nx][ny] = visited[x][y] + 1
                    q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if board[i][j] == 2 and visited[i][j] == -1:
            bfs(i,j)

# 각 칸의 최단 거리 출력
for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            print(0, end=" ")
        else:
            print(visited[i][j], end=" ")
    print()

