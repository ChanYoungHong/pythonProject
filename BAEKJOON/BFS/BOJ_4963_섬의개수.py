import sys
from collections import deque

input = sys.stdin.readline

dx = [1, -1, 0, 0, 1, -1, 1, -1]
dy = [0, 0, -1, 1, -1, 1, 1, -1]


def bfs(x, y):
    global cnt

    q = deque()
    q.append((x, y))

    cnt = 1
    while q:

        x, y = q.popleft()

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < m and 0 <= ny < n:
                if board[nx][ny] == 1:
                    board[nx][ny] = 0
                    # cnt += 1
                    q.append((nx, ny))


while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    board = [list(map(int, input().split())) for _ in range(m)]

    res = []
    tmp = 0
    for i in range(m):
        for j in range(n):

            if board[i][j] == 1:
                tmp += 1
                bfs(i, j)
                # board[i][j] = 0
                # res.append(bfs(i,j))
                # cnt = 0

    # print(sum(res))
    # print('tmp : ', tmp)
    print(tmp)