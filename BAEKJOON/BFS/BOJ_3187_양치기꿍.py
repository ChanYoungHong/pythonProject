import sys
from collections import deque

input = sys.stdin.readline

'''
1. 양 > 늑대 -> 늑대가 잡아 먹힌다.
2. 양 <= 늑대 -> 양이 잡아 먹힌다.
3. 늑대 - v, 양 - k라고 함
4.

'''
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y):
    global wolf, sheep

    q = deque()
    q.append((x, y))
    visited[x][y] = True

    while q:

        x, y = q.popleft()

        if board[x][y] == 'v':
            wolf += 1

        if board[x][y] == 'k':
            sheep += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < r and 0 <= ny < c:
                if board[nx][ny] != '#' and visited[nx][ny] == False:
                    visited[nx][ny] = True
                    q.append((nx, ny))


wolf, sheep = 0, 0
r, c = map(int, input().split())
board = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

tem1 = 0
tem2 = 0
for i in range(r):
    for j in range(c):

        if board[i][j] == '#' and visited[i][j] == False:
            bfs(i, j)

            if wolf >= sheep:
                sheep = 0
            else:
                wolf = 0

            tem1 += sheep
            tem2 += wolf

            wolf = 0
            sheep = 0

bfs(0, 0)
print(tem1, tem2)
