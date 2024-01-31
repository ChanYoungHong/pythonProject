import sys
from collections import deque

input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


# check = [[0] * m for _ in range(n)]
#
# print(check)


def bfs(a, b):
    q = deque()
    q.append((a, b))

    global cnt

    visited[a][b] = True
    while q:

        x, y = q.popleft()

        for i in range(4):
            nx = dx[i] + x
            ny = dy[i] + y

            if 0 <= nx < n and 0 <= ny < m:
                if board[nx][ny] != 'X' and not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))

                    if board[nx][ny] == 'P':
                        cnt += 1


n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
cnt = 0

for i in range(n):
    for j in range(m):

        if board[i][j] == 'I':
            bfs(i, j)

if cnt == 0:
    print('TT')
else:
    print(cnt)