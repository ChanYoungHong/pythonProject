# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# board = [list(map(int, input().split())) for _ in range(n)]
#
# dx = [-1,1,0,0]
# dy = [0,0,-1,1]
#
# visited = [[False] * n for _ in range(n)]
# white = 0
# blue = 0
#
# def dfs(x,y):
#
#     global white, blue
#
#     for i in range(4):
#         nx = dx[i] + x
#         ny = dy[i] + y
#
#         if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
#             if board[nx][ny] == 0:
#                 visited[nx][ny] = True
#                 white += 1
#                 dfs(nx, ny)
#                 return white
#
#             elif board[nx][ny] == 1:
#                 visited[nx][ny] = True
#                 blue += 1
#                 dfs(nx,ny)
#                 return blue
#
#
# ans = []
# for i in range(n):
#     for j in range(n):
#
#         if board[i][j] == 0 and not visited[i][j]:
#             visited[i][j] = True
#             ans.append(dfs(i,j))
#
# print(ans)
# print(visited)



import sys

input = sys.stdin.readline

N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]

result = []

def solution(x, y, N):
  color = paper[x][y]

  for i in range(x, x+N):
    for j in range(y, y+N):

      # print('i,j : ', i,j)
      if color != paper[i][j]:
        # print('x : ', x)
        # print('y : ', y)

        solution(x, y, N//2)
        solution(x, y+N//2, N//2)
        solution(x+N//2, y, N//2)
        solution(x+N//2, y+N//2, N//2)
        return

  if color == 0 :
    result.append(0)
  else :
    result.append(1)

solution(0,0,N)
print(result.count(0))
print(result.count(1))