from icecream import ic

# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
# graph = [list(map(int, input().split())) for _ in range(n)]
#
# dx = [-1, 1, 0]
# dy = [0, 0, -1]
#
# dp = [[0] * (n+1) for _ in range(m+1)]
# result = 0
# '''
# dp = 0 이면 방문 하지 않은 것
# dp = 1 방문한 것으로 간주
# '''
#
# def dfs(x,y):
#
#     if dp[x][y]:
#         return graph[x][y]
#
#     dp[x][y] = 0
#     for i in range(3):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx < n and 0 <= ny <= m:
#             if dp[x][y] == 0 and graph[x][y] < graph[nx][ny]:
#                 dp[x][y] = 1
#                 dp[x][y] = max(dp[x][y], graph[nx][ny] + graph[x][y])
#
#         if dp[x][y] == 1:
#             continue
#
#     return dp[x][y]
#
# for i in range(n):
#     for j in range(m):
#
#         result = max(result, dfs(i,j))
#
# print(result)
# print(dp)
#


import sys

input = sys.stdin.readline

N, M = map(int, input().strip().split())
board = [list(map(int, input().strip().split())) for i in range(N)]

# 맨 윗줄
for j in range(1, M):
    board[0][j] += board[0][j - 1]

print(board)
# 나머지
for i in range(1, N): # 1 ~ 5까지
    startLeft = [board[i][j] + board[i - 1][j] for j in range(M)]
    startRight = [board[i][j] + board[i - 1][j] for j in range(M)]

    # →
    for j in range(1, M): # 1 ~ 5까지
        startLeft[j] = max(startLeft[j], startLeft[j - 1] + board[i][j])

    # ←
    for j in range(M - 2, -1, -1): # 0 1 2 3 4
        startRight[j] = max(startRight[j], startRight[j + 1] + +board[i][j])

    # 선택
    for j in range(M):
        board[i][j] = max(startLeft[j], startRight[j])

        ic(startLeft)


print(board[-1][-1])
print(board)
print(startLeft)
print(startRight)