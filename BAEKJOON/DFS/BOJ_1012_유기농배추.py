'''
1. 시간복잡도 - 아무렇게나 구현해도 상관이 없음

'''
import sys
from collections import deque

input = sys.stdin.readline

test = int(input())

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(maps, x, y):
    q = deque()
    q.append((x, y))
    maps[x][y] = 0

    while q:
        a, b = q.popleft()
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue

            if maps[nx][ny] == 1:
                maps[nx][ny] = 0
                q.append((nx, ny))
    return


for _ in range(test):
    cnt = 0
    m, n, k = map(int, input().split())
    maps = [[0] * n for _ in range(m)]

    print(maps)
    for i in range(k):
        a, b = map(int, input().split())
        maps[a][b] = 1

    for x in range(m):
        for y in range(n):
            if maps[x][y] == 1:
                bfs(maps, x, y)
                cnt += 1

    print(cnt)

