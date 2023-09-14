import sys
from collections import deque

input = sys.stdin.readline
sys.setrecursionlimit(10000)

'''
1.
2.
3.
4.

'''

n, m, k = map(int, input().split())

# 1 2 3
# for i in range(1, n+1):
#     for j in range(1, m+1):

board = [['.'] * m for i in range(n)]
# print(board)

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(x, y):

    global cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if board[nx][ny] == '#':
                board[nx][ny] = '.'
                dfs(nx, ny)
                cnt += 1


# def bfs(x,y):
#
#     global cnt
#
#     q = deque()
#     q.append((x,y))
#
#     while q:
#
#         x,y = q.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if 0 <= nx < n and 0 <= ny < m:
#                 if board[nx][ny] == '#':
#                     board[nx][ny] = '.'
#                     cnt += 1
#                     q.append((nx,ny))
#
#     return cnt

for _ in range(k):
    r, c = map(int, input().split())

    if board[r - 1][c - 1] == '.':
        board[r - 1][c - 1] = '#'

cnt = 0
res = 0
for i in range(n):
    for j in range(m):

        if board[i][j] == '#':
            # board[i][j] = '.'
            cnt = 0
            dfs(i,j)
            res = max(res, cnt)
            # res.append(dfs(i, j))
            # res.append(bfs(i, j))
            # cnt = 1

# print(res)
# print(max(res))
print(res)

