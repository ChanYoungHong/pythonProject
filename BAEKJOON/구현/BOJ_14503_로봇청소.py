import sys
from collections import deque

input = sys.stdin.readline

# dx = [0, 0, 1, -1]
# dy = [1, -1, 0, 0]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

n, m = map(int, input().split())
y, x, d = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
cnt = 0

while 1:

    if board[y][x] == 0:
        board[y][x] = 2
        cnt += 1
    sw = False

    for i in range(4):

        ny = y + dy[d - i]
        nx = x + dx[d - i]

        if 0 <= ny < n and 0 <= nx < m:
            if board[ny][nx] == 0:
                d = (d - i + 4) % 4
                y = ny
                x = nx
                sw = True
                break

    if sw == False:

        ny = y - dy[d]
        nx = x - dx[d]

        if 0 <= ny < n and 0 <= nx < m:
            if board[ny][nx] == 1:
                break
            else:
                y = ny
                x = nx
        else:
            break

print(cnt)

# def bfs():
#     q = deque()
#     q.append((r, c))
#
#     while q:
#
#         x, y = q.popleft()
#
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or ny < 0 or nx >= n or ny >= m:
#                 continue
