import sys
from collections import deque

input = sys.stdin.readline

'''
1. 평소에는 오른쪽 밑으로 가게 했는데 
2. 일단 최댓값을 구하면 안 되나?

'''

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# def dfs(x,y):
#
#     global cnt
#     cnt = 1
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 'L':
#             board[nx][ny] = 'W'
#             dfs(nx,ny)
#             cnt += 1
#
#     return cnt
#
# cnt = 0
# res = []
# for i in range(n):
#     for j in range(m):
#
#         if board[i][j] == 'L':
#             board[i][j] = 'W'
#             res.append(dfs(i,j))
#
# print(max(res))

visited = [[0] * m for _ in range(n)]


def bfs(i, j):
    q = deque()
    q.append((i, j))

    visited[i][j] = 1
    cnt = 0

    while q:

        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] == 'L' and visited[nx][ny] == 0:
                    visited[nx][ny] = visited[x][y] + 1
                    cnt = max(cnt, visited[nx][ny])
                    q.append((nx, ny))

    return cnt


result = 0
for i in range(n):
    for j in range(m):

        if board[i][j] == 'L':
            result = max(result, bfs(i, j))

print(result)
