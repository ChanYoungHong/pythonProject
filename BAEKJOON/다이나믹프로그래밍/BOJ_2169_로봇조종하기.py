# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]

# dp = [[0] * (n + 1) for _ in range(m)]
#
# dx = [0, 0, 1]
# dy = [-1, 1, 0]
#
#
# def dfs(x, y):
#     for i in range(3):
#
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx < n and 0 <= ny < m:
#             if graph[x][y] < graph[nx][ny]:
#                 dp[x][y] += max(dp[nx][ny])
#
#
# for i in range(n):
#     for j in range(m):
#
#         if dfs(i, j) ==

import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for i in range(N)]

# 맨 윗줄
for k in range(1, M):
    board[0][k] += board[0][k - 1]

# 나머지
for i in range(1, N):  # 1 2 3 4
    startLeft = [board[i][j] + board[i - 1][j] for j in range(M)]
    print(startLeft)
    startRight = [board[i][j] + board[i - 1][j] for j in range(M)]

    # →
    for j in range(1, M):  # 1 2 3 4
        startLeft[j] = max(startLeft[j], startLeft[j - 1] + board[i][j])

    # ←
    for j in range(M - 2, -1, -1):  # 0 1 2 3 4
        startRight[j] = max(startRight[j], startRight[j + 1] + +board[i][j])

    # 선택
    for j in range(M):
        board[i][j] = max(startLeft[j], startRight[j])


print(board[-1][-1])


