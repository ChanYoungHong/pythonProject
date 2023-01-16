# from collections import deque
# import sys
#
# input = sys.stdin.readline
#
# n = int(input().rstrip())
# graph = [list(map(int, input().rstrip())) for _ in range(n)]
#
# # for _ in range(n):
# #     graph.append(list(map(int, input().rstrip())))
#
# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# visited = [[False] * n for _ in range(n)]
# result = []
# cnt2 = 0
#
# def bfs(x, y):
#     cnt = 1
#     q = deque()
#     q.append((x, y))
#     graph[x][y] = 0
#     while q:
#
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             if nx < 0 or ny < 0 or nx >= n or ny >= n:
#                 continue
#
#             if graph[nx][ny] == 0:
#                 continue
#
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 q.append((nx, ny))
#                 cnt += 1
#     result.append(cnt)
#
# for i in range(n):
#     for j in range(n):
#         if graph[i][j] == 1:
#             bfs(i, j)
#             cnt2 += 1
#
# result.sort()
#
# print(cnt2)
# for i in result:
#     print(i)


import sys

input = sys.stdin.readline

n = int(input().rstrip())
graph = [list(map(int, input().rstrip())) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
answer = []

def dfs(x, y):

    if x < 0 or y < 0 or x >= n or y >= n:
        return False

    if graph[x][y] == 1:
        global cnt
        cnt += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            dfs(nx, ny)
        return True


cnt = 0
result = 0

for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            answer.append(cnt)
            result += 1
            cnt = 0

answer.sort()
print(result)
for i in answer:
    print(i)