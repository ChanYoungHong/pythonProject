# import sys
#
# input = sys.stdin.readline
#
# '''
#
# 1. 한 칸으로 이동할 있음 -> 상하좌우 인접한 네 칸 중의 한 칸으로 이동
# 2. 새로 이동한 칸은 -> 지금까지 지나온 모든 칸에 적혀 있는 알파펫과는 달라야 한다.
# 3. 같은 알파벳은 두 번 지나갈 수 없음
#
# dfs + 백트래킹을 써야 함
#
# '''
#
# n,m = map(int, input().split())
# board = [list(input().rstrip()) for _ in range(n)]
#
# store = []
# visited = [[False] * m for _ in range(n)]
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# def dfs(x,y):
#
#
#     visited[x][y] = True
#     store.append(board[x][y])
#
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if 0 <= nx < n and 0 <= ny < m:
#             if board[nx][ny] not in store and not visited[nx][ny]:
#                 dfs(nx,ny)
#
#
# cnt = 0
# for i in range(n):
#     for j in range(m):
#
#         if board[i][j] not in store and not visited[i][j]:
#             dfs(i,j)
#             visited[i][j] = True
#             cnt += 1
#
# print(cnt)
# print(store)

import sys

input = sys.stdin.readline

'''

1. 한 칸으로 이동할 있음 -> 상하좌우 인접한 네 칸 중의 한 칸으로 이동
2. 새로 이동한 칸은 -> 지금까지 지나온 모든 칸에 적혀 있는 알파펫과는 달라야 한다.
3. 같은 알파벳은 두 번 지나갈 수 없음

dfs + 백트래킹을 써야 함

'''

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cnt = 0


def dfs(x,y,word):

    global cnt

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and board[nx][ny] not in word:
            dfs(nx,ny,word + board[nx][ny])

    if (len(word) > cnt):
        cnt = len(word)

dfs(0,0,board[0][0])
print(cnt)





