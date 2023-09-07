import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 섬을 구별해줘야 함
def bfs1(i, j):

    global cnt

    visited[i][j] = True
    board[i][j] = cnt

    q = deque()
    q.append((i, j))

    while q:

        x, y = q.popleft()

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    board[nx][ny] = cnt
                    q.append((nx, ny))


def bfs2(v):

    global answer
    dist = [[-1] * n for _ in range(n)]
    q = deque()

    for i in range(n):
        for j in range(n):

            if board[i][j] == v:
                q.append((i, j))
                dist[i][j] = 0

    while q:

        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n:
                if board[nx][ny] > 0 and board[nx][ny] != v:
                    answer = min(answer, dist[x][y])
                    # print('dist[x][y] : ', dist[x][y])
                    # print('answer : ', answer)
                    return

                if board[nx][ny] == 0 and dist[nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx,ny))


cnt = 1
visited = [[False] * n for _ in range(n)]
answer = sys.maxsize

for i in range(n):
    for j in range(n):

        if board[i][j] == 1 and not visited[i][j]:
            bfs1(i, j)
            cnt += 1

for i in range(1, cnt):
    bfs2(i)

print(answer)
